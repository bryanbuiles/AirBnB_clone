#!/usr/bin/python3
from models.engine.file_storage import FileStorage
__all__ = ["base_model", "amenity", "city",
           "place", "review", "state", "user"]
storage = FileStorage()
storage.reload()
