
#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import *
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.review import Review


place_amenity = Table(
    'place_amenity', Base.metadata,
    Column(
        'place_id',
        String(60),
        ForeignKey('places.id'),
        primary_key=True,
        nullable=False),
    Column(
        'amenity_id',
        String(60),
        ForeignKey('amenities.id'),
        primary_key=True,
        nullable=False)
)


class Place(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE") == "db") else object):
    """ A place to stay"""
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        amenity_ids = []

        reviews = relationship(
            'Review',
            backref='state',
            cascade="all, delete, delete-orphan"
        )

        amenities = relationship(
            'Amenity',
            secondary=place_amenity,
            viewonly=False
        )
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Attribute reviews that returns
            the list of Review instances"""
            from models import storage
            reviews_id = storage.all('Review')
            new_list = []
            for review in reviews_id.values():
                if review.place_id == self.id:
                    new_list.append(review)
            return new_list

        @property
        def amenities(self):
            """
            Attribute amenities that returns
            the list of Amenity instances
            """
            from models import storage
            new_list = []
            amenities_id = storage.all('Amenity').values()
            for amenity in amenities_id:
                if amenity.amenity_ids == self.id:
                    new_list.append(amenity)
            return new_list

        @reviews.setter
        def amenities(self, obj):
            """
            Handles append
            method for adding an Amenity.id
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
