#!/usr/bin/python3
"""This file contain a class thatdefines all common attributes/methods
for other classes """
import json
import cmd
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """Super clase Base"""

    def __init__(self, *args, **kwargs):
        """ Class method construtor"""
        if len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """This method allow display friendly object information
        to the user"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """This method updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the
        instance"""
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
