#!/usr/bin/python3
"""Unittest module for the BaseModel class"""
import unittest
from console import HBNBCommand
from models.state import State
from models import storage


class TestConsole(unittest.TestCase):
    """Unittests for testing BaseModel class"""
    def setUp(self):
        self.my_cmd = HBNBCommand()

    def test_create_method(self):
        """Test of console create method"""
        self.my_cmd.onecmd('create State name="Arizona"')
        my_obj = list(storage.all().values())[0]
        self.assertEqual(my_obj.name, "Arizona")


if __name__ == '__main__':
    unittest.main()
