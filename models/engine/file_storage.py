#!/usr/bin/python3
"""defines a class FileStorage 
that serializes instances to a JSON file 
and deserializes JSON file to instances
"""
import json 
from models.base_model import BaseModel
from os import path
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review



class FileStorage:
    """contain all storage classes 

    Private class attributes:
        __file_path : string - path to the JSON file .
        __objects: dictionary - empty but will store all objects by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objdict = {obj: FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)
    
    def reload(self):
        try:
            with open(FileStorage.__file_path) as f:
                self.__objects = json.load(f)
        except FileNotFoundError:
            pass