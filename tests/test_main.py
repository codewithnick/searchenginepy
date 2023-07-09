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
        self.search_engine.google()
        self.assertIsNotNone(self.search_engine.get_results())

    def test_get_results(self):
        self.search_engine.google()
        self.assertIsNotNone(self.search_engine.get_results())

if __name__ == '__main__': 
    unittest.main()