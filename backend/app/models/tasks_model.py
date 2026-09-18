from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base



#database model
#yaha hum base me apne model ke register kar rahe hai

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer,primary_key=True,index=True)
    title =Column(String(100),nullable=False)
    description = Column(String(500),nullable=False)
    is_completed = Column(Boolean,default=False)


