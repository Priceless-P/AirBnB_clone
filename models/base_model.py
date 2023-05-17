#!usr/bin/python3
"""Defines the base model class"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This is the nase model of AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initalizes a new base model.
        Args:
        *args (any): Unused.
			**kwargs (dict): Key/value pairs of attributes.
		"""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or "updated_at":
                    self.__dict__[key] = datetime.strptime(value, tform)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Updates updated_at with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns the dictionary of the base character
        It includes key/value pair __class__ representing
        the class name of the object.
        """

        basemodel_dict = self.__dict__.copy()
        basemodel_dict["created_at"] = self.created_at.isoformat()
        basemodel_dict["updated_at"] = self.updated_at.isoformat()
        basemodel_dict["__class__"] = self.__class__.__name__

    def __str__(self):
        """Returns the str represetation of the base model instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
