#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy.sql.schema import Table
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.review import Review
import models

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", backref="state", cascade="delete")

    @property
    def reviews(self):
        """returns the list of Review instances with place_id equals to the current Place.id"""
        instance = models.storage.all(Review)
        new = []
        for review in instance.values():
            if review.place_id == self.id:
                new.append(review)
        return new
