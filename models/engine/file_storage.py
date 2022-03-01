#!/usr/bin/python3
"""
Serializing instances to a JSON file and deserializing JSON files
into instances.
"""


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
    __file_path = ""
    __objects = {}

    def all(self):
        pass
