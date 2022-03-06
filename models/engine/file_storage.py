#!/usr/bin/python3
"""file storage """
import json
from models.base_model import BaseModel


class FileStorage:
    """class filestorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__,
                                             obj.id)] = obj

    def save(self):
        my_dict = {}
        for i, j in FileStorage.__objects.items():
            my_dict[i] = j.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(my_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, "r", encoding="UTF-8") as f:
                obj = json.load(f)
            for k, v in obj.items():
                class_name = k.split('.')[0]
                self.__objects[k] = eval(class_name)(**v)
        except BaseException:
            pass
