#!/usr/bin/python3
"""Defines the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User
    Attributes:
    email =  User's email
    password = User's password
    first_name = User's first name
    last_name = User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
