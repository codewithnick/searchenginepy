import unittest
from searchenginepy.DuckDuckGo import DuckduckgoScraper

class TestDuckduckgo(unittest.TestCase):
    def setUp(self):
        self.search_engine = DuckduckgoScraper()

    def test_search_returns_results(self):
        result = self.search_engine.search('test query', num_pages=1)  # Adjust the number of pages as needed
        self.assertIsNotNone(result)

    def test_getresponse_after_search(self):
        self.search_engine.search('test query', num_pages=1)  # Adjust the number of pages as needed
        result = self.search_engine.getresponse()
        self.assertIsNotNone(result)

    def test_duckduckgo(self):
        result = self.search_engine.duckduckgo()  # Assuming you have a duckduckgo method in your class
        self.assertIsNotNone(result)

    def tearDown(self):
        self.search_engine.driver.quit()

if __name__ == '__main__':
    unittest.main()
