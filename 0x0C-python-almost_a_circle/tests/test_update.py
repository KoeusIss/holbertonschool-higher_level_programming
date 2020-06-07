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
