import unittest
import sys
sys.path.insert(0, '../src')
from searchenginepy.Bing import Bing

class TestBing(unittest.TestCase):
    def setUp(self):
        self.bing = Bing()

    def test_search(self):
        result = self.bing.search('test query')
        self.assertIsNotNone(result)

    def test_getresponse(self):
        self.bing.search('test query')
        result = self.bing.getresponse()
        self.assertIsNotNone(result)

if __name__ == '__main__': 
    unittest.main()
