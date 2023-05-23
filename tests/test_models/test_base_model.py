#!/usr/bin/python3
"""
    Define unittests for 'models/base_model.py'
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)

    def test_save(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertEqual(obj_dict['created_at'], my_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], my_model.updated_at.isoformat())

    def test_str_representation(self):
        my_model = BaseModel()
        self.assertEqual(str(my_model), f"[BaseModel] ({my_model.id}) {my_model.__dict__}")

if __name__ == '__main__':
    unittest.main()
