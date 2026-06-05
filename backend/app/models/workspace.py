from sqlalchemy import String,Integer,JSON
from sqlalchemy.orm import Mapped,mapped_column
from app.db.base import Base
class Workspace(Base):
    __tablename__="workspaces"
    id:Mapped[int]=mapped_column(primary_key=True)
    user_id:Mapped[int]=mapped_column(Integer,index=True)
    name:Mapped[str]=mapped_column(String(120))
    layout:Mapped[dict]=mapped_column(JSON)
