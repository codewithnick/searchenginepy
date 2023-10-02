# __init__.py
import logging
from .Google import Google
from .Bing import Bing
from .DuckDuckGo import Duckduckgo
from .Brave import Brave

__pkgname = 'searchenginepy'
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
log.info('Initializing ' + __pkgname + ' package')

class SearchEngine:
    def __init__(self, query, pagenumber=1):
        self.query = query
        self.pagenumber = pagenumber

    def google(self):
        google_obj = Google()
        result = google_obj.search(self.query, self.pagenumber)
        return result

    def bing(self):
        bing_obj = Bing()
        result = bing_obj.search(self.query, self.pagenumber)
        return result

    def duckduckgo(self):
        duckduckgo_obj = Duckduckgo()
        result = duckduckgo_obj.search(self.query, self.pagenumber)
        return result

    def brave(self):
        brave_obj = Brave()
        result = brave_obj.search(self.query, self.pagenumber)
        return result

    def get_results(self):
        return self.results

    def get_query(self):
        return self.query
