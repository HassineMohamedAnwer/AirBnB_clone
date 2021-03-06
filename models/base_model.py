#!/usr/bin/python3
"""  first file        """
import models
import uuid
from datetime import datetime


class BaseModel:
    """ first class   """

    def __init__(self, *args, **kwargs):
        """jkhlkhlkhglghlkg"""
        tf = '%Y-%m-%dT%H:%M:%S.%f'
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value,
                                                           tf)
                elif key == "__class__":
                    continue
                self.__dict__[key] = value
        else:
            models.storage.new(self)

    def to_dict(self):
        """dictionnary"""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return (my_dict)

    def __str__(self):
        """return of class"""
        return "[{}] ({}) {}".format(__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """save method"""
        self.updated_at = datetime.now()
        models.storage.save()
