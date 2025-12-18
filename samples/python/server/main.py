import asyncio
import logging
from typing import Dict, Any, Optional
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger("Musician")

app = FastAPI()

class HctMetadata(BaseModel):
    signal: str
    from_: Optional[str] = None
    performance: Optional[Dict[str, Any]] = None

    class Config:
        extra = "ignore"

@app.post("/tasks/send")
async def handle_task(request: Request):
    body = await request.json()
    message = body.get("message", {})
    parts = message.get("parts", [])
    
    # Defaults
    tempo = "moderato"
    dynamics = "mf"
    signal = "unknown"

    # Extract HCT metadata
    for part in parts:
        metadata = part.get("metadata", {})
        if "hct" in metadata:
            hct = metadata["hct"]
            signal = hct.get("signal", signal)
            perf = hct.get("performance", {})
            tempo = perf.get("tempo", tempo)
            dynamics = perf.get("dynamics", dynamics)
    
    logger.info(f"Received Signal: {signal.upper()} | Tempo: {tempo.upper()} | Dynamics: {dynamics.upper()}")

    # Simulate HCT behaviors
    
    # 1. Tempo (Latency/Depth)
    delay = 0.0
    if tempo == "largo":
        delay = 2.0
        logger.info("Tempo is LARGO. Taking time for deep thought...")
    elif tempo == "presto":
        delay = 0.1
        logger.info("Tempo is PRESTO. Rushing response!")
    
    await asyncio.sleep(delay)

    # 2. Dynamics (Resource/Verbosity)
    response_text = "Task acknowledged."
    if dynamics == "ff":
        response_text += " [Chain of Thought: Analysis complete. All constraints satisfied. Confidence 0.99.]"
    elif dynamics == "pp":
        response_text = "Ack."

    return {
        "jsonrpc": "2.0",
        "id": body.get("id"),
        "result": {
            "message": {
                "role": "model",
                "parts": [{"type": "text", "text": response_text}]
            }
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
