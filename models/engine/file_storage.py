#!/usr/bin/python3
"""
Serializing instances to a JSON file and deserializing JSON files
into instances.
"""


import json
from re import X
from models.base_model import BaseModel


class FileStorage:
    """ Class that works serializing and deserializing objects
    from JSON and to JSON.

    Att:
    __file_path: string - path to the JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id

    Methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects
    (only if the JSON file (__file_path) exists ; otherwise, do nothing.
    If the file doesn't exist, no exception should be raised)

    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ Returns the objects dictionary """
        return self.__objects

    def new(self, obj):
        """ Updates the objects dictionary with a new object"""
        return self.__objects.update({type(obj).__name__ + '.' + obj.id: obj})

    def save(self):
        """ Saves the dictionary into a json file """
        new_dict = {}
        try:
            with open(self.__file_path, mode="w") as file:
                for key, value in self.__objects.items():
                    # Saving objects into __obj dict
                    new_dict[key] = value.to_dict()
                    # "converting" value from obj inst to dict att
                json.dump(new_dict, file)
                # Getting all into a new file
        except Exception:
            return

    def reload(self):
        """ Loads an object from json file if it exists,
            otherwise do nothing
        """
        try:
            with open(self.__file_path, mode="r") as file:
                # Opens file containing json repr of instances
                attrs = json.load(file)
            for key, value in attrs.items():
                # Instantiates the objects loaded from the JSON
                self.__objects[key] = eval(str(key).split(".")[2](**value))()
        except Exception:
            return
