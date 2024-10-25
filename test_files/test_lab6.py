import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab6_count_vowels import count_vowels

class TestLab1(unittest.TestCase):

    def test(self):
        #count_vowels should take in a string and return the number of vowels in the string
        self.assertEqual(count_vowels("Hello, world!"), 3)
        self.assertEqual(count_vowels("abcdefghijklmnopqrstuvwxyz"), 5)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)
        self.assertEqual(count_vowels("Cinco Ranch High School"), 6)
        



if __name__ == '__main__':
    unittest.main()