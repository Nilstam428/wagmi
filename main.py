from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from datetime import datetime
from typing import Optional
from json.decoder import JSONDecodeError
import json
import uvicorn


app = FastAPI()

@app.post("/wagmi")
async def wagmi(request: Request):
    try:
        body = await request.json()
    except (json.JSONDecodeError, ValueError):
        body = {}

    if not body:
        return {
            "message": "wagmi",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "lang": "Python"
        }

    a: Optional[float] = body.get("a")
    b: Optional[float] = body.get("b")

    if (
        not isinstance(a, (int, float)) or
        not isinstance(b, (int, float)) or
        a < 0 or b < 0 or (a + b) > 100
    ):
        return JSONResponse(status_code=400, content={"error": "Invalid input"})

    return {
        "result": a + b,
        "a": a,
        "b": b,
        "status": "success"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
