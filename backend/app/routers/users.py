from fastapi import APIRouter,Depends
from app.api.current_user import get_current_user
router=APIRouter(prefix="/users",tags=["users"])
@router.get("/me")
def me(user=Depends(get_current_user)):return {"id":user.id,"email":user.email}
