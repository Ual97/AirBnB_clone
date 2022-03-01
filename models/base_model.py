#!/usr/bin/python3
"""
Created class Base Model, attributes and methods.
"""


import uuid
from datetime import date, datetime


class BaseModel:
    """ Base Model class itself 

        Att:
        id: randomly generated id, unique for each instance.
        created_at: original time in which the instance was created.
        updated_at: this will update every time save method runs.

        Methods:
        __init__: instancing with or without dictionary.
        __str___: a string representation of an instance.
        save: updates the public instance attribute updated_at with the current datetime
        to_dict: returns a dictionary containing all keys/values of __dict__ of the instance.

    """ 

    def __init__(self, *args, **kwargs):
        """ Instance constructor that can receive dictionary """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key in kwargs:
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """ String representation of instance"""
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
    
    def save(self):
        """ updates public instance attribute updated_at"""
        self.updated_at = datetime.now()
    
    def to_dict(self):
        """ Instance to a JSON string """
        new_dict = self.__dict__.copy()
        new_dict.update({'created_at':self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
        'updated_at':self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"), '__class__':'BaseModel'})
        return new_dict