import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab2_letterr import letterr

class TestLab1(unittest.TestCase):

    def test(self):
        self.assertEqual(letterr("pluh"), "First letter is p and last letter is h")
        self.assertEqual(letterr("brisket"), "First letter is b and last letter is t")
        self.assertEqual(letterr("hello"), "First letter is h and last letter is o")
        self.assertEqual(letterr("second"), "First letter is s and last letter is d")
        self.assertEqual(letterr("first"), "First letter is f and last letter is t")
        self.assertEqual(letterr("last"), "First letter is l and last letter is t") 

        



if __name__ == '__main__':
    unittest.main()