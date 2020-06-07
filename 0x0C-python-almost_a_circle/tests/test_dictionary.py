"""TestDictionary"""
import unittest
from models.rectangle import *
from models.base import *
from models.square import *


class TestDictionaryRepresentatin(unittest.TestCase):
    """Tests class for dictoinary representation"""

    def test_dictionary_representation_for_rectangle(self):
        """test to_dictionary method"""
        r = Rectangle(2, 3, 4, 5, 122)
        dic_r = {"id": 122, "width": 2, "height": 3, "x": 4, "y": 5}
        self.assertDictEqual(r.to_dictionary(), dic_r)
