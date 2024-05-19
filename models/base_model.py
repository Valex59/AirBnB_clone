#!/usr/bin/python3
"""
BaseMoedel
This module defines the BaseModel class, which acts as the foundational class
for all other classes in the AirBnB clone project.
"""
# This module defines a BaseModel class used as parent for other classes
from datetime import datetime
import uuid

class BaseModel:
    """Defines BaseModel class with public attributes:

    id: a string representing the unique id of the instance of the BaseModel
    created_at: a datetime object representing the creation date of the
                instance of the BaseModel
    updated_at: a datetime object representing the last update date of
                the instance of the BaseModel
    """

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel instance

        Args:
            *args: list of arguments
            **kwargs: dictionary of arguments
        Note: each instance of BaseModel create should have a unique 'id'.
        define public instance 'created_at'.
        assign datetime value to 'created_at' when instance is created.
        define public 'updated_at'.
        assign 'updated_at' with latest datetime when instance is updated.
        __str__ should print: [<class name>] (<self.id>) <self.__dict__>.
        define 'save(self)' method that updates the 'updated_at' attribute.
        define public instance method 'to_dict' which returns a dictionary.
        containing all keys/values of '__dict__'.
        to_dict returns it's dictionary by using 'self.__dict__.
        only set instance attribute will be returned.
        the dictionary would contain key __class__ that holds classname
        of the object.
        use statement 'varible = datetime.isoformat()' to convert
        'created_at' and 'updated_at' to string object.
        Create a dictionary representation of BaseModel with "simple object type"

        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
                else:
                    continue
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """A string representation of the BaseModel is returned."""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

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
