#!/usr/bin/python3
"""
Current file: review.py
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    place_id = ''  # it will be the Place.id
    user_id = ''  # it will be the User.id
    text = ''
