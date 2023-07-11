#Duckduckgo class which has functions to search and get results
import requests 
import bs4
class Duckduckgo():
    def __init__(self):
        """_summary_
        """
        print('search engine : DuckDuckGo')
        self.url = 'https://duckduckgo.com/'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.results = []
        self.payload={}
    def search(self,query ,pagenumber=1) -> list:
        self.payload['q']=query #query parameter to Duckduckgo
        self.payload['start']=(pagenumber-1)*10 #pagenumber parameter to Duckduckgo (does not work)
        """_summary_

        Args:
            query (_type_): _description_

        Returns:
            list: list of links from Duck search
        """
        r = requests.get(self.url, headers=self.headers)
        if r.status_code == 200:
            self.results.append(r.text)
        else:
            self.results.append('Unable to get results')
        #parse results using bs4
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        soup.find_all('a')
        links=[i.get('href') for i in soup.find_all('a')]
        return links
    def getresponse(self):
        return self.results