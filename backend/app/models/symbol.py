from sqlalchemy import String
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class Symbol(Base):
    __tablename__="symbols"
    id:Mapped[int]=mapped_column(primary_key=True)
    ticker:Mapped[str]=mapped_column(String(32),unique=True,index=True)
    name:Mapped[str]=mapped_column(String(255))
    market:Mapped[str]=mapped_column(String(64),default="MOEX")
