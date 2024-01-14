#!/usr/bin/python3
"""This module includes a number of tests on the FileStorage functionalities
to ensure that everything works as expected"""
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Make tests for FileStorage class implementation"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.bm = BaseModel()

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_new_sets_obj(self):
        """Test that new() sets an object to dictionary"""
        bm = BaseModel()
        self.storage.new(bm)
        objects = self.storage.all()
        key = 'BaseModel.' + bm.id
        self.assertIn(key, objects)
        self.assertEqual(objects[key], bm)

    def test_save(self):
        """Test that save() serializes objects to the JSON file"""
        self.storage.new(self.bm)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))

    def test_reload(self):
        """Test that reload() deserializes the JSON file to objects"""
        self.storage.new(self.bm)
        self.storage.save()
        self.storage.reload()
        objects = self.storage.all()
        key = 'BaseModel.' + self.bm.id
        self.assertIn(key, objects)
        self.assertEqual(objects[key].to_dict(), self.bm.to_dict())

    def test_create_class_from_dictionary(self):
        """Test creating a Class from a dictionary using **kwards concept"""
        self.bm.name = "My_First_Model"
        self.bm.my_number = 89
        bm_json = self.bm.to_dict()
        new_bm = BaseModel(**bm_json)
        self.assertIsInstance(new_bm.created_at, datetime)


if __name__ == '__main__':
    unittest.main()
