#!/usr/bin/python3

'''
    Test unit for user model
'''

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUserModel(unittest.TestCase):
    '''
        Class Test User Model
    '''

    def test_user_model_inhertie(self):
        '''
            tests that the User class Inherits from BaseModel
        '''
        nu = User()
        self.assertIsInstance(nu, BaseModel)

    def test_user__model_params(self):
        '''
            test param user model
        '''

        nu = User()
        self.assertTrue("last_name" in nu.__dir__())
        self.assertTrue("first_name" in nu.__dir__())
        self.assertTrue("email" in nu.__dir__())
        self.assertTrue("password" in nu.__dir__())

    def test_user_first_name(self):
        '''
            Test the type of name
        '''
        new = User()
        name = getattr(new, "first_name")
        self.assertIsInstance(name, str)

    def test_user_last_name(self):
        '''
            test equal type last name 
        '''
        new = User()
        name = getattr(new, "last_name")
        self.assertIsInstance(name, str)

    def test_user_email(self):
        '''
            test equal type email 
        '''
        new = User()
        name = getattr(new, "email")
        self.assertIsInstance(name, str)

    
    def test_user_password(self):
        '''
            test equal type last name 
        '''
        new = User()
        name = getattr(new, "password")
        self.assertIsInstance(name, str)

