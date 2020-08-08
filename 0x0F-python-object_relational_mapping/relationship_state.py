#!/usr/bin/python3
"""
State module
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """State model class"""
    __tablename__ = 'states'
    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                unique=True,
                nullable=False
                )
    name = Column(String(128),
                  nullable=False
                  )
    cities = relationship(
        "City",
        cascade="all, delete",
        backref='state'
    )
