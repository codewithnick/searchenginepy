# __init__.py
# #importing google class
from .Google import Google
from .Bing import Bing
from .DuckDuckGo import Duckduckgo
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
    def bing(self):
        bingobj=Bing()
        result=bingobj.search(self.query)
        return result
    def duckduckgo(self):
        duckduckgoobj=Duckduckgo()
        result=duckduckgoobj.search(self.query)
        return result
    def brave(self):
        braveobj=Brave()
        result=braveobj.search(self.query)
        return result
    def get_results(self):
        return self.results

    def get_query(self):
        return self.query
