from fastapi import APIRouter
router=APIRouter(prefix="/watchlist",tags=["watchlist"])
@router.get("/")
def get_watchlist():return {"symbols":["SBER","GAZP","Si"]}
