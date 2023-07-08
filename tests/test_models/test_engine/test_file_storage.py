#!/usr/bin/python3
'''Unit tests for the BaseModel class.'''
import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    '''Represents TestFileStorage class.'''

    def setUp(self):
        '''Set up any data needed for the test.'''
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.base_model.save()

    def tearDown(self):
        '''Clean up any resources used during the test.'''
        self.storage.delete(self.base_model)
        del self.storage
        del self.base_model

    def test_all_method(self):
        '''Test the all() method of FileStorage.'''
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIn('BaseModel.{}'.format(self.base_model.id), all_objects)

    def test_new_method(self):
        '''Test the new() method of FileStorage.'''
        new_model = BaseModel()
        self.storage.new(new_model)
        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)

    def test_save_method(self):
        '''Test the save() method of FileStorage.'''
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()
        file_path = self.storage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))
        with open(file_path, 'r') as file:
            data = file.read()
            self.assertIn('BaseModel.{}'.format(new_model.id), data)

    def test_reload_method(self):
        '''Test the reload() method of FileStorage.'''
        new_model = BaseModel()
        self.storage.new(new_model)
        self.storage.save()

        # Clear storage and load from file
        self.storage = FileStorage()
        self.storage.reload()

        all_objects = self.storage.all()
        self.assertIn('BaseModel.{}'.format(new_model.id), all_objects)

    def test_delete_method(self):
        '''Test the delete() method of FileStorage.'''
        self.storage.delete(self.base_model)
        all_objects = self.storage.all()
        self.assertNotIn('BaseModel.{}'.format(self.base_model.id),
                         all_objects)

    def test_delete_method_with_nonexistent_object(self):
        '''Test the delete() method of FileStorage with a
            nonexistent object.
        '''
        new_model = BaseModel()
        self.storage.delete(new_model)
        all_objects = self.storage.all()
        self.assertNotIn('BaseModel.{}'.format(new_model.id), all_objects)


if __name__ == '__main__':
    unittest.main()
