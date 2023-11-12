#!/usr/bin/python3
"""
define the stat model
"""
from .base_model import BaseModel

class Place(BaseModel):
    """
    define place model for the airbnb clon
    """
    city_id: str
    user_id: str
    name: str
    description: str
    number_rooms: int
    number_bathrooms: int
    max_guest: int
    price_by_night: int
    latitude: float
    longitude: float
    amenity_ids: int
