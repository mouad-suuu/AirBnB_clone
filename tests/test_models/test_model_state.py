#!/usr/bin/python3
''' 
Class test Unit state Model

'''
import unittest
import datetime
from models.state import State
from models.base_model import BaseModel



class TestStateModel(unittest.TestCase):
    '''
    Class Test Unit State Model

    '''

    @classmethod
    def setUp(clas):
        '''
        set up class test state model
        
        '''
        clas.stat = State()
        clas.stat.name = "Paris"

    @classmethod
    def tearDown(clas):
        '''
        clean test after run

        '''
        del clas.stat

    def test_class_exists_state_model(self):
        '''
        Tests if class exists
        '''
        res = "<class 'models.state.State'>"
        self.assertEqual(str(type(self.stat)), res)

    def test_inheritance_state_model(self):
        '''
        test inheristance from base model

        '''
        self.assertIsInstance(self.stat, State)
        self.assertEqual(type(self.stat), State)
        self.assertEqual(issubclass(self.stat.__class__, BaseModel), True)

    def test_types_state_model(self):
        '''
        test type state model

        '''
        self.assertIsInstance(self.stat.id, str)
        self.assertEqual(type(self.stat.id), str)
        self.assertIsInstance(self.stat.name, str)
        self.assertIsInstance(self.stat.created_at, datetime.datetime)
        self.assertIsInstance(self.stat.updated_at, datetime.datetime)
       

    def test_save_state_model(self):
        '''
        test if updated at not equal to created at
        '''
        self.stat.save()
        self.assertNotEqual(self.stat.created_at, self.stat.updated_at)

    def test_functions(self):
        '''Test if State module is documented.
        '''
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        '''
        test if params exists
        '''
        self.assertTrue(hasattr(self.stat, 'id'))
        self.assertTrue(hasattr(self.stat, 'name'))
        self.assertTrue(hasattr(self.stat, 'created_at'))
        self.assertTrue(hasattr(self.stat, 'updated_at'))
        

    def test_to_dict_state_model(self):
        '''
        test if to dict is working
        '''
        mj = self.stat.to_dict()

        self.assertEqual(str, type(mj['created_at']))
        self.assertEqual(mj['created_at'],self.stat.created_at.isoformat())

        self.assertEqual(datetime.datetime, type(self.stat.created_at))
        self.assertEqual(mj['__class__'],self.stat.__class__.__name__)

        self.assertEqual(mj['id'], self.stat.id)

    def test_id_unique_state_model(self):
        '''
        test if class got unique id from inhersite class

        '''
        sta2 = self.stat.__class__()
        sta3 = self.stat.__class__()
        sta4 = self.stat.__class__()
        sta5 = self.stat.__class__()
        self.assertNotEqual(self.stat.id, sta2.id)
        self.assertNotEqual(self.stat.id, sta3.id)
        self.assertNotEqual(self.stat.id, sta4.id)
        self.assertNotEqual(self.stat.id, sta5.id)


if __name__ == '__main__':
    unittest.main()

