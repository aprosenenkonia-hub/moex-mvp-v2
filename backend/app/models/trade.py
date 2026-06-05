from datetime import datetime
from sqlalchemy import DateTime,Numeric,BigInteger,String
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class Trade(Base):
    __tablename__="trades"
    id:Mapped[int]=mapped_column(primary_key=True)
    symbol:Mapped[str]=mapped_column(String(32),index=True)
    ts:Mapped[datetime]=mapped_column(DateTime,index=True)
    price:Mapped[float]=mapped_column(Numeric)
    volume:Mapped[int]=mapped_column(BigInteger)
    side:Mapped[str]=mapped_column(String(8))
