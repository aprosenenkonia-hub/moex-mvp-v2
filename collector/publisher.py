import json,redis
from config import REDIS_HOST,REDIS_PORT
redis_client=redis.Redis(host=REDIS_HOST,port=REDIS_PORT,decode_responses=True)
def publish_quote(quote:dict):redis_client.publish("quotes",json.dumps(quote))
