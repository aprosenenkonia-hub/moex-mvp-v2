from fastapi import Depends,HTTPException
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.core.jwt import decode_token
from app.models.user import User
security=HTTPBearer()
def get_current_user(credentials=Depends(security),db:Session=Depends(get_db)):
    payload=decode_token(credentials.credentials)
    if not payload:raise HTTPException(status_code=401,detail="Invalid token")
    user=db.get(User,int(payload["sub"]))
    if not user:raise HTTPException(status_code=401,detail="User not found")
    return user
