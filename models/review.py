#!/usr/bin/python3
"""
Module containing 'review' class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creates new review
    """
    place_id = ""
    user_id = ""
    text = ""
