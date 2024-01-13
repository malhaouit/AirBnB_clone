#!/usr/bin/python3
"""
Current file: city.py
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class City that inherits from BaseModel"""

    state_id = ''  # it will be the State.id
    name = ''
