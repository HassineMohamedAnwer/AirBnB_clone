#!/usr/bin/python3
"""  first file        """
import uuid
from datetime import datetime

class BaseModel:
    """ first class   """

    def __init__(self, *args, **kwargs):
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        return (my_dict)
