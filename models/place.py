#!/usr/bin/python3
""" Place Module for HBNB project """
from msilib import Table
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import models
from models.review import Review

place_amenity = Table('place_amenity',
                      Base.metadata,
                      Column("place_id",
                             String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id",
                             String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
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
        """Returns the list of Review instances with
        place_id equals to the current Place.id"""
        instances = models.storage.all(Review)
        new = []
        for review in instances.values():
            if review.place_id == self.id:
                new.append(review)
        return new

