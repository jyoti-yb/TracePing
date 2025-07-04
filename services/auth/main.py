from fastapi import FastAPI, Request, Response
from middleware import FlowMarkMiddleware

app = FastAPI()
app.add_middleware(FlowMarkMiddleware, service_name="auth")

@app.get("/")
async def auth_endpoint():
    return {"status": "auth ok"}
