#!/usr/bin/python3
"""
This module defines the FileStorage class
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objs, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                FileStorage.__objects = json.load(f)
                for key, value in FileStorage.__objects.items():
                    class_name = key.split('.')[0]
                    FileStorage.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Calls reload() for deserializing the JSON file to objects
        """
        self.reload()
