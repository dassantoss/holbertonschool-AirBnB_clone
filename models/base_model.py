#!/usr/bin/python3
'''Define BaseModel'''


import uuid
from datetime import datetime


class BaseModel:
    '''Represents a BaseModel class that defines
        common attributes and methods for other classes.
    '''

    def __init__(self, *args, **kwargs):
        '''Initialize a new instance of BaseModel.'''
        if kwargs:
            for key, item in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        item = datetime.strptime(item, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, item)
        else:
            self.id = str(uuid.uuid4())
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
