import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab4_name_format import first_last
from lab4_name_format import last_first

class TestLab1(unittest.TestCase):

    def test(self):
        #last_first should return "lastname, firstname"
        self.assertEqual(last_first("John Doe"), "Doe, John")
        self.assertEqual(last_first("Jane Smith"), "Smith, Jane")
        self.assertEqual(last_first("Elmer Fudd"), "Fudd, Elmer")

        #first_last should return "firstname lastname"
        self.assertEqual(first_last("Doe, John"), "John Doe")
        self.assertEqual(first_last("Smith, Jane"), "Jane Smith")
        self.assertEqual(first_last("Fudd, Elmer"), "Elmer Fudd")

        #first_last and last_first should be inverses of each other
        self.assertEqual(first_last(last_first("John Doe")), "John Doe")
        self.assertEqual(first_last(last_first("Jane Smith")), "Jane Smith")
        self.assertEqual(first_last(last_first("Elmer Fudd")), "Elmer Fudd")

        self.assertEqual(last_first(first_last("Doe, John")), "Doe, John")    
        self.assertEqual(last_first(first_last("Smith, Jane")), "Smith, Jane")
        self.assertEqual(last_first(first_last("Fudd, Elmer")), "Fudd, Elmer")



if __name__ == '__main__':
    unittest.main()