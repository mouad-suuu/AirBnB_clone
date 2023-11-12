#!/usr/bin/python3
"""
define the stat model
"""
from models.base_model import BaseModel

class User(BaseModel):
     # Represents a user in the system
    username: str # Unique identifier for the user
    password: str # Password for the user
    first_name: str # User's first name
    last_name: str # User's last name
    email: str # User's email address
