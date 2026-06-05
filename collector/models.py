from datetime import datetime
from sqlalchemy import DateTime,Numeric,BigInteger,String
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
class Base(DeclarativeBase):pass
class Candle(Base):
    __tablename__="candles"
    id:Mapped[int]=mapped_column(primary_key=True)
    symbol:Mapped[str]=mapped_column(String(32),index=True)
    timeframe:Mapped[str]=mapped_column(String(16),default="1m")
    ts:Mapped[datetime]=mapped_column(DateTime,index=True)
    open:Mapped[float]=mapped_column(Numeric)
    high:Mapped[float]=mapped_column(Numeric)
    low:Mapped[float]=mapped_column(Numeric)
    close:Mapped[float]=mapped_column(Numeric)
    volume:Mapped[int]=mapped_column(BigInteger,default=0)
