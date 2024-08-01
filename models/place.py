#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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
    reviews = relationship("Review", cascade="all, delete-orphan",
                           backref="place")
    amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False,
                             back_populates="place_amenities")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Gettter atribute that returns the list of Review instances"""
            reviews_list = []
            for review_val in models.storage.all(Review).values():
                if review_val.place_id == self.id:
                    reviews_list.append(review_val)
            return reviews_list

        @property
        def amenities(self):
            """Gettter atribute that returns the list of  instances"""
            amen_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amen_list.append(amenity)
            return amen_list

        @amenities.setter
        def amenities(self, am_obj):
            """
            Setter attributethat handles append method for
            adding an Amenity.id to the attribute amenity_ids
            """
            if type(am_obj) == Amenity:
                self.amenity_ids.append(am_obj.id)
