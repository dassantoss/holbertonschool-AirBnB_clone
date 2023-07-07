#!/usr/bin/python3
'''Define BaseModel'''


import uuid
from datetime import datetime


class BaseModel:
    '''Represents a BaseModel class that defines
        common attributes and methods for other classes.
    '''

    def __init__(self):
        '''Initialize a new instance of BaseModel.'''
        self.id = str(uuid.uuid4)
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        '''Update the updated_at attribute with the current datetime.'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''Return a dictionary representation of the BaseModel object.'''
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        '''Return a string representation of the BaseModel object.'''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
