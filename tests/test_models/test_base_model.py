#!/usr/bin/python3
"""base_model.py module"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
    def test_created_at_ISO(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.created_at, ISO)
    
