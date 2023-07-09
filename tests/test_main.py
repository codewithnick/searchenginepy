import unittest
import sys
sys.path.insert(0, '../src')
from searchenginepy import SearchEngine

class TestSearchEngine(unittest.TestCase):
    def setUp(self):
        self.search_engine = SearchEngine('test query')

    def test_get_query(self):
        self.assertEqual(self.search_engine.get_query(), 'test query')

    def test_google(self):
        result = self.search_engine.google()
        self.assertIsNotNone(result)

    def test_bing(self):
        result = self.search_engine.bing()
        self.assertIsNotNone(result)  

    def test_duckduckgo(self):
        result = self.search_engine.duckduckgo()
        self.assertIsNotNone(result)

    def test_brave(self):
        result = self.search_engine.brave()
        self.assertIsNotNone(result)

    def test_get_results(self):
        self.search_engine.google()
        result = self.search_engine.get_results()
        self.assertIsNotNone(result)

if __name__ == '__main__': 
    unittest.main()