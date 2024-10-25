import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab5_replaceString import replaceString

class TestLab1(unittest.TestCase):

    def test(self):
        #replaceString should take in a string, a target string, and a replacement string
        # and replace all instances of the target string with the replacement string
        self.assertEqual(replaceString("Hello, world!", "world", "planet"), "Hello, planet!")
        self.assertEqual(replaceString("Hello, world!", "Hello", "Goodbye"), "Goodbye, world!")
        self.assertEqual(replaceString("Hello, world!", "!", "?"), "Hello, world?")
        self.assertEqual(replaceString("Hello, world!", " ", ""), "Hello,world!")
        self.assertEqual(replaceString("Cinco Ranch High School", "Cinco Ranch", "Smelly Lakes"), "Smelly Lakes High School")
        self.assertEqual(replaceString("Cinco Ranch High School", "High School", "Elementary"), "Cinco Ranch Elementary")



if __name__ == '__main__':
    unittest.main()