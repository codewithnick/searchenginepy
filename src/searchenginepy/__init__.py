# __init__.py
# #importing google class
from .Google import Google
from .Bing import Bing
from .DuckDuckGo import DuckDuckGo
from .Brave import Brave
import logging
__pkgname='searchenginepy'
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

log.info('Initializing '+__pkgname+' package')

class SearchEngine:
    def __init__(self, query):
        self.query = query
        self.results = []
    def google(self):
        googleobj=Google()
        result=googleobj.search(self.query)
        return result
    def get_results(self):
        return self.results

    def get_query(self):
        return self.query
