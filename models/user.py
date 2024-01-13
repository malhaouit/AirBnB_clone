#!/usr/bin/python3
"""
This module covers the users of the BaseModel class.
Current file: user.py
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from the BaseModel class"""

    email = ''
    password = ''
    first_name = ''
    last_name = ''
