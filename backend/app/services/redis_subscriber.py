import json,asyncio
from app.core.redis import redis_client
from app.websocket.connection_manager import manager
async def subscribe_quotes():
    pubsub=redis_client.pubsub(); pubsub.subscribe("quotes")
    while True:
        msg=pubsub.get_message(ignore_subscribe_messages=True)
        if msg:
            await manager.broadcast({"type":"quote","data":json.loads(msg["data"])})
        await asyncio.sleep(0.05)
