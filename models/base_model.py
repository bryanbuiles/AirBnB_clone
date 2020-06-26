#!/usr/bin/python3
""" Base.py """
import json
import cmd
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """super clase Base
    """

    def __init__(self, *args, **kwargs):
        """ construtor """
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
        """ display the str object information """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update date """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ dictionary """
        dic = self.__dict__.copy()
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
