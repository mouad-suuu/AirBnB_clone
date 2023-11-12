#!/usr/bin/python3

'''
    Test base model functions 
'''
import datetime
import unittest
import sys
from models.base_model import BaseModel
from io import StringIO




class TestBaseModel(unittest.TestCase):
    '''
      Test Unit Base Model 
    '''

    def setUp(self):
        '''
            Set up instance Base Model 
        '''
        self.my_model = BaseModel()
        self.my_model.name = "Ahmed Yak"


    def test_equal_id_type(self):
        '''
            assertEqual that the type of the id is string
        '''
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))


    def test_name_model(self):
        '''
            checks name of instance base model
        '''
        self.assertEqual("Ahmed Yak", self.my_model.name)

    def test_equal_created_updated_year(self):
        '''
            assert Equal updated and created year
        '''
        self.assertEqual(self.my_model.updated_at.year,self.my_model.created_at.year)

    def test_save_base_model(self):
        '''
            checks updated with new updated date
        '''
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_str_base_model(self):
        '''
            check equal print of base model 
        '''
        b = sys.stdout
        id_base_model = self.my_model.id
        strIO = StringIO()
        sys.stdout = strIO
        print(self.my_model)

        cap = strIO.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(id_base_model))

        sys.stdout = b

    def test_to_dict_type_base_model(self):
        '''
            check to dict return right type 

        '''

        self.assertEqual("<class 'dict'>",str(type(self.my_model.to_dict())))

    def test_to_dict_class_base_model(self):
        '''
            check class exist

        '''

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_created_at_base_model(self):
        '''
            Checks the type of the value of created_at.
        '''
        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_updated_at(self):
        '''
            Checks the type of the value of updated_at.
        '''
        self.assertEqual("<class 'str'>",str(type((self.my_model.to_dict())["updated_at"])))

    

    def test_kwargs_instantiation(self):
        '''
            Test that an instance is created using the
            key value pair.
        '''
        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        '''
            test new model created at

        '''
        md = self.my_model.to_dict()
        nm = BaseModel(md)
        self.assertTrue(isinstance(nm.created_at, datetime.datetime))

    def test_type_updated_at(self):
        '''
            test new model updated at

        '''
        md = self.my_model.to_dict()
        nm = BaseModel(md)
        self.assertTrue(isinstance(nm.updated_at, datetime.datetime))

    def test_equal_dict_base_model(self):
        '''
            test new model and actual model are equal
        '''
        md = self.my_model.to_dict()
        nm = BaseModel(**md)
        nmd = nm.to_dict()
        self.assertEqual(md, nmd)

    def test_not_equal_base_model(self):
        '''
            test that new model not equal to actual model
        '''
        md = self.my_model.to_dict()
        nm = BaseModel(md)
        self.assertNotEqual(self.my_model, nm)

