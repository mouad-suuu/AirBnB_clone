#!/usr/bin/python3
"""
Class TestConsoleAirbnbClone for unit test Airbnb Console

"""
import sys
import unittest
from io import StringIO
from console import HBNBCommand


class TestConsoleAirbnbClone(unittest.TestCase):
    """
    Test unit for HBNBCommand class

    """
    def setUp(self):
        '''setup for'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def createInstanceHBNBCommand(self):
        ''' 
        create an instance of the HBNBCommand class
        '''
        return HBNBCommand()
    
    def test_quit_console(self):
        ''' 
        test quit function console
        '''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF_console(self):
        ''' 
        test EOF exists
        '''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all_console(self):
        ''' 
        test all exists
        '''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))
    
    def test_show_console(self):
        '''
        test show all console 
        '''
        c = self.create()
        c.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        c.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    def test_create_console(self):
        '''
        test create user console
        '''
        c = self.create()
        c.onecmd("create User")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

