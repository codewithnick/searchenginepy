#Brave class which has functions to search and get results
import requests 
import bs4
class Brave():
    def __init__(self):
        """_summary_
        """
        print('search engine : Brave')
        self.url = 'https://search.brave.com/search'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.httpallowed=True
        self.results = []
        self.payload={}
    def search(self,query,pagenumber=1) -> list:
        self.payload['q']=query #query parameter to Brave
        self.payload['offset']=(pagenumber-1) #pagenumber parameter to Brave
        """_summary_

        Args:
            query (_type_): _description_

        Returns:
            list: list of links from Brave search
        """
        r = requests.get(self.url, headers=self.headers,params=self.payload)
        if r.status_code == 200:
            self.results.append(r.text)
        else:
            self.results.append('Unable to get results')
        #parse results using bs4
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        soup.find_all('a')
        links=[i.get('href') for i in soup.find_all('a')]
        links=self.cleanlinks(links)
        return links
    def cleanlinks(self,links):
        #clean links
        links=[i for i in links if i is not None]
        if self.httpallowed:
            links=[i for i in links if i.startswith('http')]
        else:
            links=[i for i in links if i.startswith('https')]
        return links
    def getresponse(self):
        return self.results