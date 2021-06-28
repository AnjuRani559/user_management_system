from sqlalchemy import Table, Column, Integer, String, DateTime
from app import db  # noqa
from .interface import UserInterface
#from click import DateTime
from datetime import datetime
from typing import Any


class User(db.Model):


    __tablename__ = "user"

    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    full_name = Column(String(255))
    salary = Column(Integer())
    created_at = Column(DateTime, nullable=False, default=datetime.now)

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self


