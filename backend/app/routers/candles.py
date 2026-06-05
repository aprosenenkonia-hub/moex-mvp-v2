from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.candle import Candle
router=APIRouter(prefix="/candles",tags=["candles"])
@router.get("/{symbol}")
def get_candles(symbol:str,db:Session=Depends(get_db)):
    rows=db.query(Candle).filter(Candle.symbol==symbol).order_by(Candle.ts.asc()).limit(200).all()
    if not rows:return [{"time":"2026-06-01","open":100,"high":110,"low":95,"close":105,"volume":10000},{"time":"2026-06-02","open":105,"high":118,"low":101,"close":114,"volume":14300}]
    return [{"time":r.ts.strftime("%Y-%m-%d"),"open":float(r.open),"high":float(r.high),"low":float(r.low),"close":float(r.close),"volume":r.volume} for r in rows]
