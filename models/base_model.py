#!/usr/bin/python3
"""base_model module"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class definitio

    Attributes:
        id (string): Unique identifier
        created_at (datetime): date created
        updated_at (datetime): date updated

    """

    def __init__(self, *args, **kwargs):
        """Initializes a base model instance"""

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
        else:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key != '__class__':
                    setattr(self, key, value)

    def __str__(self):
        """Returns class name, id and dictionary"""

        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Updates the pblic instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance:"""
        new_dict = {}
        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
