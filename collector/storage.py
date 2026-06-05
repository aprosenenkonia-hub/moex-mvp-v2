from db import SessionLocal
from models import Candle
def save_candle(data:dict):
    db=SessionLocal(); c=Candle(symbol=data["symbol"],timeframe=data["timeframe"],ts=data["ts"],open=data["open"],high=data["high"],low=data["low"],close=data["close"],volume=data["volume"]); db.add(c); db.commit(); db.close()
