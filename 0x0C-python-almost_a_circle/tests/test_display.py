"""TestDisplay"""
import unittest
from models.base import *
from models.rectangle import *
import sys
import io


class TestDisplay(unittest.TestCase):
    """tests display rectangle"""
    pass


class TestStrRepresentation(unittest.TestCase):
    """tests __str__ overriding methods"""

    def setUp(self):
        self.r = Rectangle(4, 6, 2, 1, 12)
        self.r0 = Rectangle(4, 6)

    def tearDown(self):
        del self.r
        del self.r0

    def test_str_representation(self):
        str_r = self.r.__str__()
        self.assertEqual(str_r, "[Rectangle] (12) 2/1 - 4/6")

    def test_str_representation_with_default_value(self):
        str_r = self.r0.__str__()
        self.assertEqual(str_r, "[Rectangle] (6) 0/0 - 4/6")
