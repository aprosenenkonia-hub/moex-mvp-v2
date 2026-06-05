from sqlalchemy import String,Boolean,Integer,JSON
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class Alert(Base):
    __tablename__="alerts"
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(Integer,index=True)
    symbol:Mapped[str]=mapped_column(String(32))
    condition:Mapped[dict]=mapped_column(JSON)
    active:Mapped[bool]=mapped_column(Boolean,default=True)
