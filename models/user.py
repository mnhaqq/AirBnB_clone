#!/usr/bin/python3
"""
Module containing 'User' class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Creates new user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
