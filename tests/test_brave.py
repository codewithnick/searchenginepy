import unittest
import sys
sys.path.insert(0, '../src')

from searchenginepy.Brave import Brave

class TestBrave(unittest.TestCase):
    def setUp(self):
        self.brave = Brave()

    def test_search(self):
        result = self.brave.search('test query')
        self.assertIsNotNone(result)

    def test_getresponse(self):
        self.brave.search('test query')
        result = self.brave.getresponse()
        self.assertIsNotNone(result)

if __name__ == '__main__': 
    unittest.main()
