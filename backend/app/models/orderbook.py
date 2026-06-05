from datetime import datetime
from sqlalchemy import DateTime,Numeric,BigInteger,String
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class OrderBookSnapshot(Base):
    __tablename__="orderbook"
    id:Mapped[int]=mapped_column(primary_key=True)
    symbol:Mapped[str]=mapped_column(String(32),index=True)
    ts:Mapped[datetime]=mapped_column(DateTime,index=True)
    bid_price:Mapped[float]=mapped_column(Numeric)
    bid_volume:Mapped[int]=mapped_column(BigInteger)
    ask_price:Mapped[float]=mapped_column(Numeric)
    ask_volume:Mapped[int]=mapped_column(BigInteger)
