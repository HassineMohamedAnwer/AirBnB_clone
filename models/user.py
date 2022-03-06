#!/usr/bin/python3
"""class user"""
from models.base_model import BaseModel


class User(BaseModel):
    """inherits from basemodel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
