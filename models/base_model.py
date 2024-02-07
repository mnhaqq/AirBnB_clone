#!/usr/bin/python3
"""
Module containing BaseModel class
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes and methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes base object
        """
        if kwargs:
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
        """
        Returns string representation of object
        """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updatea public instance attribute "updated_at" with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns dictionary containing all key value pairs of __dict__
        """
        self.__dict__['__class__'] = type(self).__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
