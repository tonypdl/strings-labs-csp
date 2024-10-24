import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab1_concat import concat

class TestLab1(unittest.TestCase):

    def test_leapYear(self):
        self.assertEqual(concat("pluh", "bruh"), "pluh bruh")
        self.assertEqual(concat("brisket", "dumpling"), "brisket dumpling")
        self.assertEqual(concat("hello", "world"), "hello world")
        self.assertEqual(concat("second", "third"), "second third")
        self.assertEqual(concat("first", "last"), "first last")

        



if __name__ == '__main__':
    unittest.main()