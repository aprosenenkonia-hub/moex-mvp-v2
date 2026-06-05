from fastapi import APIRouter
router=APIRouter(prefix="/market",tags=["market"])
@router.get("/oi/{symbol}")
def get_open_interest(symbol:str):return {"symbol":symbol,"value":123456,"change":1245}
@router.get("/delta/{symbol}")
def get_delta(symbol:str):return {"symbol":symbol,"delta":2456}
@router.get("/orderbook/{symbol}")
def get_orderbook(symbol:str):return {"symbol":symbol,"bids":[{"price":284.90,"volume":1200},{"price":284.80,"volume":950},{"price":284.70,"volume":780}],"asks":[{"price":285.10,"volume":1100},{"price":285.20,"volume":870},{"price":285.30,"volume":640}]}
