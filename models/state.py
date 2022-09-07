#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id"""
            cities = storage.all(City)
            city_list = []

            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
