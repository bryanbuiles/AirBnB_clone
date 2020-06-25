#!/usr/bin/python3
""" Base.py """
import json
import cmd
from datetime import datetime
from uuid import uuid4


class BaseModel():
    """supper clase Base
    """

    def __init__(self, id=str(uuid4()),
                 created_at=datetime.now(), updated_at=datetime.now()):
        """ contrutor """
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        """ display the str object information """
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ update de date """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ dictionary """
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return self.__dict__
