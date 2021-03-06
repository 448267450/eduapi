from sqlalchemy import Column
from sqlalchemy import Integer, String

from models import db


class User(db.Model):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    phone = Column(String(30),
                  unique=True,
                  nullable=False)
    auto_key = Column(String(100), nullable=False)
    nick_name = Column(String(20))
    photo = Column(String(100))