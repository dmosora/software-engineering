# Implementation, should be in another file, but for
# illustrative purposes, it's defined here

def append_to_list(lst, new_val):
    """ Does not change original list, like Python's append(). """
    new_list = (len(lst) + 1) * [None] # Allocate new list
    for i, val in enumerate(lst):
        new_list[i] = val
    new_list[len(new_list) - 1] = new_val
    return new_list

def list_sort(lst):
    """ Bubble sort implementation. VERY SLOW, would not recommend... """
    new_list = lst.copy() # Also copy original list
    for i in range(0, len(new_list)):
        for j in range(i, len(new_list)):
            if new_list[i] > new_list[j]:
                temp = new_list[j]
                new_list[j] = new_list[i]
                new_list[i] = temp
    return new_list

# Tests for the above implementation
import unittest # pylint:disable=wrong-import-position

class TestPythonCode(unittest.TestCase):
    """
    These tests are speccing out our custom implementations of the same Python standard library code.
    """
    def test_list_append(self):
        starting_list = []
        result = append_to_list(starting_list, "a")
        self.assertEqual(result, ["a"])
        self.assertNotEqual(result, starting_list)

    def test_list_sort(self):
        starting_list = [4, 2, 7, 1]
        result = list_sort(starting_list)
        self.assertEqual(result, [1, 2, 4, 7])
        self.assertNotEqual(result, starting_list)