from fastapi import APIRouter
router=APIRouter(prefix="/symbols",tags=["symbols"])
@router.get("/")
def get_symbols():return ["SBER","GAZP","LKOH","ROSN","Si","RTS"]
