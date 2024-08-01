#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Gettter atribute that returns City objects"""
            cities_obj = []
            for city_val in models.storage.all(City).values():
                if city_val.state_id == self.id:
                    cities_obj.append(city_val)
            return cities_obj
