import unittest

class TestPythonCode(unittest.TestCase):
    """
    These tests are evaluating code that is part of the Python standard library.
    Framework code is assumed to be tested already, so these aren't testing much.
    CPython's test suite: https://github.com/python/cpython/tree/master/Lib/test
    """
    def test_list_append(self):
        starting_list = []
        starting_list.append("a")
        self.assertEqual(starting_list, ["a"])

    def test_list_sort(self):
        starting_list = [4, 2, 7, 1]
        starting_list.sort()
        self.assertEqual(starting_list, [1, 2, 4, 7])
