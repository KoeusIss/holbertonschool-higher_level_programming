"""TestUpdate"""
import unittest
from models.base import *
from models.rectangle import *


class TestUpdate(unittest.TestCase):
    """Tests rectangle update"""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10)

    def tearDown(self):
        del self.r

    def test_updates_id_attributes(self):
        """tests id attribute update"""
        self.r.update(98)
        self.assertEqual(self.r.id, 98)

    def test_updates_width_attributes(self):
        """tests width attribute update"""
        self.r.update(98, 2)
        self.assertEqual(self.r.width, 2)

    def test_updates_height_attributes(self):
        """tests height attribute update"""
        self.r.update(98, 2, 3)
        self.assertEqual(self.r.height, 3)

    def test_updates_x_attributes(self):
        """tests x attribute update"""
        self.r.update(98, 2, 3, 4)
        self.assertEqual(self.r.x, 4)

    def test_updates_y_attributes(self):
        """tests y attribute update"""
        self.r.update(98, 2, 3, 4, 5)
        self.assertEqual(self.r.y, 5)

    def test_update_height_on_explicit_call(self):
        """tests height update on explicit call"""
        self.r.update(height=1)
        self.assertEqual(self.r.height, 1)

    def test_update_two_attribute_width_x_on_explicit_call(self):
        """test update two attribute on explicit call"""
        self.r.update(width=1, x=2)
        self.assertEqual(self.r.width, 1)
        self.assertEqual(self.r.x, 2)

    def test_update_many_attributes_on_explicit_unorder_call(self):
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(self.r.width, 2)
        self.assertEqual(self.r.id, 89)
        self.assertEqual(self.r.x, 3)
        self.assertEqual(self.r.y, 1)

    def test_update_mixin_args_kwargs(self):
        self.r.update(100, 101, 102, x=103, y=104)
        self.assertEqual(self.r.id, 100)
        self.assertEqual(self.r.width, 101)
        self.assertEqual(self.r.height, 102)
        self.assertEqual(self.r.x, 103)
        self.assertEqual(self.r.y, 104)
