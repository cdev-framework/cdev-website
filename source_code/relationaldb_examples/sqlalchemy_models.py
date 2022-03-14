from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base

import sqlalchemy_aurora_data_api

sqlalchemy_aurora_data_api.register_dialects()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    
    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}"

