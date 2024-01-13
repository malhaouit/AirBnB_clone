"""This module includes a number of tests on the BaseModel functionalities
to ensure that everything still works as expected"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Set up for the tests"""
        self.bm = BaseModel()
        self.bm.name = "My First Model"
        self.bm.my_number = 89

    def tearDown(self):
        """Clean up after each test"""
        del self.bm

    def test_uuid(self):
        """Test that ids are uniq and set correctly"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_attributes_are_set_correctly(self):
        """Test that attributes are set correctly"""
        self.assertEqual(self.bm.name, "My First Model")
        self.assertEqual(self.bm.my_number, 89)

    def test_to_dict_method(self):
        """Test that to_dict returns the correct dictionary"""
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["name"], "My First Model")
        self.assertEqual(bm_dict["my_number"], 89)
        self.assertEqual(bm_dict["__class__"], "BaseModel")

    def test_str_method(self):
        """Test that __str__ returns the correct string"""
        bm_str = str(self.bm)
        self.assertTrue("[BaseModel] (" in bm_str)
        self.assertTrue("'name': 'My First Model'" in bm_str)
        self.assertTrue("'my_number': 89" in bm_str)

    def test_save_method(self):
        """ """
        first_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(self.bm.updated_at, first_updated_at)

    def test_creating_model_from_dictionary(self):
        """Test that a BaseModel is correctly created from a dictionary"""
        base_model = BaseModel()
        base_model.name = 'Base Model'
        base_model.my_num = 113
        base_model.save()
        bm_dict = base_model.to_dict()
        new_base_model = BaseModel(**bm_dict)
        new_bm_dict = new_base_model.to_dict()
        self.assertEqual(new_bm_dict['__class__'], 'BaseModel')
        self.assertEqual(new_bm_dict['name'], 'Base Model')
        self.assertEqual(new_bm_dict['my_num'], 113)
        self.assertEqual(new_bm_dict['created_at'], bm_dict['created_at'])
        self.assertEqual(new_bm_dict['updated_at'], bm_dict['updated_at'])


if __name__ == '__main__':
    unittest.main()
