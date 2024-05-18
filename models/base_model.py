#!/usr/bin/python3
"""
BaseMoedel
This module defines the BaseModel class, which acts as the foundational class
for all other classes in the AirBnB clone project.
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    A base class for all models of this AirBnb clone project.

    Attributes:
        id (str): Each BaseModel instance is assigned a unique id created with
        uuid4 of the uuid builtin module.
        created_at (datetime): assigns the datetime through datetime builtin
        at it's creation.
        updated_at (datetime): assigns athe datetime which updates at the
        creation of any object.
    """

    def __init__(self):
        """A new instance of BaseModel is initialized."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """A string representation of the BaseModel is returned."""
        return "[{}] ({}) {}".format(self.__class__.__name__, 
                self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' wth thw current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns the dictionary representation of the BaseModel instance.
        This dictionary consists of all instance attributes, a
        __class__ key with the class name,
        and datetime attributes formatted in ISO strings.
        """
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = self.__class__.__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
