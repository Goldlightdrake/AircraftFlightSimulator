from unittest import TestCase

from main import hello


class Test(TestCase):
    def test_hello(self):
        assert hello() == "hello"
