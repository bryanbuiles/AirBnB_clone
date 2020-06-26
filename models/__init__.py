#!/usr/bin/python3
from models.engine.file_storage import FileStorage
__all__ = ["base_model"]


storage = FileStorage()
storage.reload()
