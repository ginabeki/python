# this file is not for production since it is a test file
# pylint, pylakess
# autopep8, standard style guide for python
# built in module for test, unittest
import unittest
import unittest1
class TestMain(unittest.TestCase):
    def test_do_staff(self):
        test_param = 10
        result = unittest1.do_staff(test_param)
        self.assertEqual(result, 15)

unittest.unittest1()