#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[self.__class__.__name__ + ".id"] = obj
    def save(self):
        with open(self.__file_path, mode='a', encoding="utf-8") as f:
            f.write(json.dumps(self.__objects))

    def reload(self):
        try:   
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                self.__objects = json.loads(f)
        except:
            pass
