#google class which has functions to search and get results
import requests 
import bs4
class Google():
    def __init__(self):
        """_summary_
        """
        print('search engine : google')
        self.url = 'https://www.google.com/search?q='
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.results = []
    def search(self,query ) -> list:
        """_summary_

        Args:
            query (_type_): _description_

        Returns:
            list: list of links from google search
        """
        r = requests.get(self.url+query, headers=self.headers)
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