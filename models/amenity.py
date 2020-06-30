#!/usr/bin/python3
"""This file contain a class ibhritanse from BaseModel"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class inheritance from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        super().__init__(*args, **kwargs)
