#!/usr/bin/python3
"""
This module defines a base class for
all models in our hbnb clone
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class that defines common attributes and methods for other classes.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        - Assigns a unique id using uuid.uuid4() converted to a string.
        - Sets the created_at and updated_at attributes to the current datetime.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel object.
        The string includes the class name, id, and the object's dictionary representation.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object.
        The dictionary includes all attributes of the object, including the class name, id,
        and the converted string representations of created_at and updated_at attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
