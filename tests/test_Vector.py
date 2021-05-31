from unittest import TestCase

from lib.classes.Vector import Vector


class TestVector(TestCase):
    def test_init_valid_arguments(self):
        #given valid arguments should return Vector obj
        self.assertTrue(isinstance(Vector(3,4), Vector))

    def test_init_invalid_arguments(self):
        #given one argument should raise TypeError
        with self.assertRaises(TypeError):
            Vector(3)
