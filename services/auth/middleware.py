import time
from starlette.middleware.base import BaseHTTPMiddleware

class FlowMarkMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, service_name):
        super().__init__(app)
        self.service_name = service_name

    async def dispatch(self, request, call_next):
        start = time.perf_counter()
        header = request.headers.get("X-FlowMark", "")
        parts = header.split(" → ") if header else []

        try:
            response = await call_next(request)
            status = "ok" if response.status_code < 500 else f"fail{response.status_code}"
        except Exception:
            status = "fail500"
            raise
        finally:
            duration = round((time.perf_counter() - start) * 1000)
            hop = f"{self.service_name}:{status}:{duration}ms"
            parts.append(hop)
            response.headers["X-FlowMark"] = " → ".join(parts)

        return response
