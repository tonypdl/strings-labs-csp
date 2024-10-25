import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab3_substring import substring

class TestLab1(unittest.TestCase):

    def test(self):
        self.assertEqual(substring('hello', 2, 4), 'll')
        self.assertEqual(substring('hello', 0, 1), 'h')
        self.assertEqual(substring('hello', 0, 4), 'hell')
        self.assertEqual(substring('computer science', 6, 10), 'er s')
        self.assertEqual(substring('computer science', 0, 2), 'co')
        self.assertEqual(substring('computer science', 0, 10), 'computer s')

        



if __name__ == '__main__':
    unittest.main()