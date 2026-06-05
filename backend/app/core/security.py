from datetime import datetime,timedelta
from jose import jwt
from app.core.config import settings
def create_access_token(user_id:int):
    return jwt.encode({"sub":str(user_id),"exp":datetime.utcnow()+timedelta(days=7)},settings.JWT_SECRET,algorithm=settings.JWT_ALGORITHM)
