"""TestBase module"""
import unittest


from models.base import *

class TestBase(unittest.TestCase):
    """Tests the base class"""

    def test_creation_base_instance(self):
        b = Base()
        self.assertIsInstance(b, Base)

    def test_creation_base_instance_without_id_arg(self):
        b = Base()
        self.assertEqual(b.id, 2)

    def test_creation_two_base_instance_without_id_arg(self):
        a = Base()
        b = Base()
        self.assertEqual(b.id, 4)

    def test_creation_base_instance_with_id_arg(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

if __name__ == "__main__":
    unittest.main()
