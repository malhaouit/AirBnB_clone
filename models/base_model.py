#!/usr/bin/python3
"""
This module includes the Base class for other sub-classes.
Current file: base_model.py
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """ The BaseModel class defines all common attributes/methods
    for other sub-classes """
    def __init__(self, *args, **kwargs):
        """ Initializes BaseModel instances attributes """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
            return

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        """ Formatts a simple human readable info about BaseModel object """
        class_name = self.__class__.__name__
        id_str = self.id
        return "[{}] ({}) {}".format(class_name, id_str, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at
        with the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__
        of the instance """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
