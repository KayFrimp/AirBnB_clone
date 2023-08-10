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

    def __init__(self):
        """Initializes a base model instance"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Returns class name, id and dictionary"""

        return f"[{self.__class__.__name__}] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """Updates the pblic instance attribute updated_at"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values
            of __dict__ of the instance:"""
        pass
