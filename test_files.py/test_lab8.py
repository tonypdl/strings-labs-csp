import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lab8_count_words import count_words

class TestLab1(unittest.TestCase):

    def test(self):
        self.assertEqual(count_words("Hello, world!"), 2)
        self.assertEqual(count_words("It was the best of times, it was the worst of times."), 12)
        self.assertEqual(count_words("I have a dream."), 4)
        self.assertEqual(count_words("Cinco Ranch High School"), 4)
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog."), 9)
        self.assertEqual(count_words("The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."), 18)
        self.assertEqual(count_words(""), 0)
        self.assertEqual(count_words("blue whale baluga"), 3)

        



if __name__ == '__main__':
    unittest.main()