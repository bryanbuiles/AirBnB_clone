#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage():

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        dic = {}
        for k, v in self.__objects.items():
            dic[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding="utf-8") as f:
                des = json.load(f)
                for i in des:
                    self.__objects[i] = BaseModel(**des[i])
        except:
            pass
