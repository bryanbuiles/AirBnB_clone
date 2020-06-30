#!/usr/bin/python3
"""This file contain a class ibhritanse from BaseModel"""
import models
from models.base_model import BaseModel


class Review(BaseModel):
    """Class inheritance from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        super().__init__(*args, **kwargs)
