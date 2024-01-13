#!/usr/bin/python3
"""
Current file: file_storage.py
"""
import json
import os
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """ Serializes instances to a JSON file and deserializes
    JSON file to instances """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                dict_objs = json.load(f)
            for key, value in dict_objs.items():
                if value['__class__'] == 'BaseModel':
                    self.__objects[key] = BaseModel(**value)
                elif value['__class__'] == 'User':
                    self.__objects[key] = User(**value)