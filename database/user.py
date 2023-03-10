from .db_gino import BaseModel
from sqlalchemy import Column, String, BigInteger, sql


class User(BaseModel):
    __tablename__ = "users"
    user_id = Column(BigInteger, primary_key=False)
    hotels = Column(String(500), primary_key=False)
    command = Column(String(200), primary_key=False)
    date = Column(String(200), primary_key=False)

    query: sql.select

