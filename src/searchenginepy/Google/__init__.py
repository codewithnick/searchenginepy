#google class which has functions to search and get results
import requests 
import bs4
class Google():
    def __init__(self):
        """_summary_
        """
        print('search engine : google')
        self.url = 'https://www.google.com/search'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        #self.httpallowed=True
        self.results = []
        self.payload={}
    def search(self,query ,pagenumber=1) -> list:
        self.payload['q']=query #query parameter to google
        self.payload['start']=(pagenumber-1)*10 #pagenumber parameter to google
        """_summary_

        Args:
            query (_type_): _description_

        Returns:
            list: list of links from google search
        """
        r = requests.get(self.url,params=self.payload, headers=self.headers)
        if r.status_code == 200:
            self.results.append(r.text)
        else:
            self.results.append('Unable to get results')
        #parse results using bs4
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        soup.find_all('a')
        links=[i.get('href') for i in soup.find_all('a')]
        #links=self.cleanlinks(links)
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