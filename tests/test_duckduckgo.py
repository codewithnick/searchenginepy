import unittest
import sys
sys.path.insert(0, '../src')
from searchenginepy.DuckDuckGo import Duckduckgo

class TestDuckduckgo(unittest.TestCase):
    def setUp(self):
        self.duckduckgo = Duckduckgo()

    def test_search_returns_results(self):
        result = self.duckduckgo.search('test query')
        self.assertIsNotNone(result)

    def test_getresponse_after_search(self):
        self.duckduckgo.search('test query')
        result = self.duckduckgo.getresponse()
        self.assertIsNotNone(result)

if __name__ == '__main__': 
    unittest.main()
