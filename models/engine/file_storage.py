#!/usr/bin/python3
"""
Defines 'FileStorage' class
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    Serializes instances to json and deserializes json to instances
    """

    __file_path = 'file.json'
    __objects = dict()
    class_dict = {"BaseModel": BaseModel,
                  "User": User,
                  "Place": Place,
                  "State": State,
                  "City": City,
                  "Amenity": Amenity,
                  "Review": Review}

    def all(self):
        """
        Returns dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in '__objects' the obj with key '<obj class name>.id'
        """
        key = f"{type(obj).__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes '__objects' to the json file path
        """
        dic = dict()

        for key, value in self.__objects.items():
            dic[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(dic, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects if it exists
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dic = json.load(f)

            for key, value in dic.items():
                class_name = value['__class__']
                class_type = self.class_dict[class_name]
                obj = class_type(**value)
                self.__objects[key] = obj
        except Exception:
            pass
