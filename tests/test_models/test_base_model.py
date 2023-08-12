#!/usr/bin/python3
"""base_model.py module"""

import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_id_is_string(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
    def test_unique_id(self):
        bm_1 = BaseModel()
        bm_2 = BaseModel()
        self.assertNotEqual(bm_1.id, bm_2.id)
    def test_created_at_is_datetime(self):
        base_model = BaseModel()
        self.assertIs(type(base_model.created_at), datetime)
    def test_to_dict(self):
        bm = BaseModel();
        bm.name = "My First Model"
        bm.my_number = 89
        bm_json = bm.to_dict()
        self.assertIs(type(bm_json), dict)
