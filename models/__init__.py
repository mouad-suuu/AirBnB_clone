#!/usr/bin/python3
from models.engine.file_storage import FileStorage
from .base_model import BaseModel

# Create a unique FileStorage instance for the application
storage = FileStorage()
storage.reload()
