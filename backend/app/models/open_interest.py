from datetime import datetime
from sqlalchemy import DateTime,BigInteger,String
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class OpenInterest(Base):
    __tablename__="open_interest"
    id:Mapped[int]=mapped_column(primary_key=True)
    symbol:Mapped[str]=mapped_column(String(32),index=True)
    ts:Mapped[datetime]=mapped_column(DateTime,index=True)
    value:Mapped[int]=mapped_column(BigInteger)
