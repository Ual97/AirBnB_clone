#!/usr/bin/python3
"""
Serializing instances to a JSON file and deserializing JSON files
into instances.
"""


import json


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

    @property
    def all(self):
        """ """
        return self.__objects


    def new(self, obj):
        """ """
        self.__objects.update({type(obj).__name__ + '.' + obj.id:obj})
    
    def save(self):
        """ """
        with open(self.__file_path, mode="w") as file:
            json.dump(self.__objects, file)


    def reload(self):
        """ """
        try:
            if self.__file_path:
                with open(self.__file_path, mode="r") as file:
                    self.__objects = json.load(file)
        except(FileNotFoundError):
            return