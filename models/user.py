#!/usr/bin/python3
"""This file contain a class ibhritanse from BaseModel"""
import models
from models.base_model import BaseModel


class User(BaseModel):
    """Class inheritance from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor method"""
        super().__init__(*args, **kwargs)
