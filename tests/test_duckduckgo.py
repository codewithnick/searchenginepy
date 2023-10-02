import unittest
from searchenginepy.DuckDuckGo import DuckduckgoScraper

class TestDuckduckgo(unittest.TestCase):
    def setUp(self):
        self.duckduckgo = DuckduckgoScraper()

    def test_search_returns_results(self):
        result = self.duckduckgo.search('test query', num_pages=1)  # Adjust the number of pages as needed
        self.assertIsNotNone(result)

    def test_getresponse_after_search(self):
        self.duckduckgo.search('test query', num_pages=1)  # Adjust the number of pages as needed
        result = self.duckduckgo.getresponse()
        self.assertIsNotNone(result)

    def tearDown(self):
        self.duckduckgo.driver.quit()

if __name__ == '__main__':
    unittest.main()
