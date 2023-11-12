#!/usr/bin/python3
"""
define the stat model
"""
from .base_model import BaseModel

class Review(BaseModel):
    """
    define review table
    """
    user_id: int
    place_id: int
    text: str
