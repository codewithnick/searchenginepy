import unittest
import sys
sys.path.insert(0, '../src')
from searchenginepy.Google import Google

class TestGoogle(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def setUp(self):
        self.google = Google()

    def test_search(self):
        result = self.google.search('test query')
        self.assertIsNotNone(result)

    def test_getresponse(self):
        self.google.search('test query')
        result = self.google.getresponse()
        self.assertIsNotNone(result)

if __name__ == '__main__': 
    unittest.main()