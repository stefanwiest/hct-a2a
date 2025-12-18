import httpx
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Conductor")

SERVER_URL = "http://localhost:8000/tasks/send"

async def send_hct_task(signal: str, tempo: str, dynamics: str, task_id: str):
    payload = {
        "jsonrpc": "2.0",
        "method": "tasks/send",
        "id": task_id,
        "message": {
            "role": "user",
            "parts": [{
                "type": "text",
                "text": "Analyze market trends.",
                "metadata": {
                    "hct": {
                        "signal": signal,
                        "from": "Conductor",
                        "performance": {
                            "tempo": tempo,
                            "dynamics": dynamics
                        }
                    }
                }
            }]
        }
    }
    
    logger.info(f"Sending {signal.upper()} ({tempo}, {dynamics})...")
    async with httpx.AsyncClient() as client:
        response = await client.post(SERVER_URL, json=payload, timeout=10.0)
        logger.info(f"Response: {response.json()['result']['message']['parts'][0]['text']}")

async def main():
    # 1. Start with a Cue, Allegro (fast), MF (normal)
    await send_hct_task("cue", "allegro", "mf", "1")
    
    # 2. Slow down for deep thought: Largo, FF (verbose)
    await send_hct_task("cue", "largo", "ff", "2")

    # 3. Quick check: Presto, PP (minimal)
    await send_hct_task("cue", "presto", "pp", "3")

if __name__ == "__main__":
    asyncio.run(main())
