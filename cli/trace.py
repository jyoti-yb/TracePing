import requests
import uuid
import json
from pathlib import Path

def trace(url: str):
    req_id = str(uuid.uuid4())[:8]
    headers = {"X-FlowMark": f"req={req_id},path="}
    resp = requests.get(url, headers=headers)

    trace = resp.headers.get("X-FlowMark")
    print(f"🧭 Flow ID: {req_id}")
    print(f"🧠 Trace: {trace}")

    Path("traces").mkdir(exist_ok=True)
    with open(f"traces/{req_id}.flow", "w") as f:
        json.dump({"url": url, "trace": trace}, f)
