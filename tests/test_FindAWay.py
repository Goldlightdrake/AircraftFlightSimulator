from unittest import TestCase

from lib.classes.FindAWay import FindAWay
from lib.classes.Vector import Vector


class TestFindAWay(TestCase):
    def test_calculate_path_the_same_points(self):
        #given two the same points should return 0
        self.assertEqual(FindAWay.calculate_path((3,3), (3,3)), 0)

    def test_calculate_path_normal_input(self):
        #given two normal points should return vector object
        self.assertTrue(isinstance(FindAWay.calculate_path((1,4), (2,5)), Vector))

    def test_calculate_path_invalid_input(self):
        #given invalid input to func should raise TypeError
        with self.assertRaises(TypeError):
            FindAWay.calculate_path((3,3,3), (3))

    def test_calculate_path_str_arguments(self):
        #given str arguments should return normal Vector object
        self.assertTrue(isinstance(FindAWay.calculate_path(('3', '3'), ('1', '-3')), Vector))


    def test_calculate_path_one_argument(self):
        #given only one argument should raise TypeError
        with self.assertRaises(TypeError):
            FindAWay.calculate_path((1,3))