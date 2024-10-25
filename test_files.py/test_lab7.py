import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab7_reverse_string import reverse_string

class TestLab1(unittest.TestCase):

    def test(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("world"), "dlrow")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string("racecar"), "racecar")
        self.assertEqual(reverse_string("madam"), "madam")
        self.assertEqual(reverse_string("a"), "a")
        self.assertEqual(reverse_string("Cinco Ranch High School"), "loohcS hgiH hcnaR ocniC")

        



if __name__ == '__main__':
    unittest.main()