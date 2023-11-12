#!/usr/bin/python3
''' 
Class test Unit file storage

'''

import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage



class TestFileStorage(unittest.TestCase):
    '''unit test class for file storage '''

    @classmethod
    def setUp(clas):
        ''' 
        set up class test file storage

        '''
        clas.fs = FileStorage()

    @classmethod
    def tearDown(clas):
        '''
        clean test after run

        '''
        del clas.fs

    def test_class_file_storage(self):
        '''
        test if class excits

        '''
        res = "<class 'models.engine.file_storage.FileStorage'>"
        self.assertEqual(str(type(self.fs)), res)

    def test_types_file_storage(self):
        '''
        test type from review model

        '''
        self.assertIsInstance(self.fs, FileStorage)
        self.assertEqual(type(self.fs), FileStorage)

    def test_doc_fiel_storage(self):
        '''
        test if review string out works

        '''
        self.assertIsNotNone(FileStorage.__doc__)

    def test_save_file_storage(self):
        '''
        test if updated at work after save

        '''
        self.fs.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        self.assertEqual(storage.all(), storage._FileStorage__objects)

    def test_reload_file_storage(self):
        '''
        teste reload file storage works
        
        '''
        self.fs.save()
        self.assertEqual(os.path.exists(storage._FileStorage__file_path), True)
        o = storage.all()
        FileStorage._FileStorage__objects = {}
        self.assertNotEqual(o, FileStorage._FileStorage__objects)
        storage.reload()
        for k, v in storage.all().items():
            self.assertEqual(o[k].to_dict(), v.to_dict())


if __name__ == '__main__':
    unittest.main()

