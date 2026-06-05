from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.schemas.user import UserCreate,UserLogin
from app.schemas.token import Token
from app.repositories.user_repository import UserRepository
from app.services.auth_service import hash_password,verify_password
from app.core.security import create_access_token
router=APIRouter(prefix="/auth",tags=["auth"])
@router.post("/register",response_model=Token)
def register(payload:UserCreate,db:Session=Depends(get_db)):
    if UserRepository.get_by_email(db,payload.email):raise HTTPException(status_code=400,detail="User exists")
    user=UserRepository.create(db,payload.email,hash_password(payload.password)); return Token(access_token=create_access_token(user.id))
@router.post("/login",response_model=Token)
def login(payload:UserLogin,db:Session=Depends(get_db)):
    user=UserRepository.get_by_email(db,payload.email)
    if not user or not verify_password(payload.password,user.password_hash):raise HTTPException(status_code=401,detail="Invalid credentials")
    return Token(access_token=create_access_token(user.id))
