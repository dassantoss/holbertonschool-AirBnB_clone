#!/usr/bin/python3
'''Unit tests for the BaseModel class.'''
import unittest
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    '''Represents TestBaseModel class.'''

    def setUp(self):
        '''Set up any data needed for the test.'''
        storage.clear()
        self.my_model = BaseModel

    def tearDown(self):
        '''Clean up any resorces used during the test.'''
        del self.my_model

    def test_initial_attributes(self):
        '''Test the initial attributes of a BaseModel instance.'''
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save_method(self):
        '''Test the save() method of a BaseModel instance.'''
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        '''Test the to_dict() method of a BaseModel instance'''
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        self.assertEqual(my_model_json['__class__'], 'BaseModel')
        self.assertEqual(my_model_json['name'], 'My First Model')
        self.assertEqual(my_model_json['my_number'], 89)

    def test_str_method(self):
        '''Test the __str__() method of a BaseModel instance'''
        my_model = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(my_model.id,
                                                       my_model.__dict__)
        self.assertEqual(str(my_model), expected_output)

    def test_create_from_dict(self):
        '''Test creating a BaseModel instance from a dictionary'''
        my_model_dict = {
            'id': '1234',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:00:00.000000',
            'name': 'My Model',
            'my_number': 42
        }
        my_model = BaseModel(**my_model_dict)

        self.assertEqual(my_model.id, '1234')
        self.assertEqual(my_model.created_at.year, 2023)
        self.assertEqual(my_model.created_at.month, 1)
        self.assertEqual(my_model.created_at.day, 1)
        self.assertEqual(my_model.updated_at.year, 2023)
        self.assertEqual(my_model.updated_at.month, 1)
        self.assertEqual(my_model.updated_at.day, 1)
        self.assertEqual(my_model.name, 'My Model')
        self.assertEqual(my_model.my_number, 42)


if __name__ == '__main__':
    unittest.main()
