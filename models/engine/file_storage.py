#!/usr/bin/python3
"""This file include a class that allow storage classes, serializate and
deserializates to JSON"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

allclases = {"BaseModel": BaseModel, "User": User, "State": State,
    "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}


class FileStorage():
    """class that allow storage classes, serializate and
    deserializates to JSON"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """This method return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """This method sets in __objects the obj with key <obj class name>.id
        Args:
            - Input method"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """This method serializes __objects to the JSON file (path: __file_path)"""
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """This method deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                des = json.load(f)
                for i in des:
                    self.__objects[i] = allclases[des[i]
                                                  ["__class__"]](**des[i])
        except:
            pass
