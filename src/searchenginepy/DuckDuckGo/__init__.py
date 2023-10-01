#Duckduckgo class which has functions to search and get results
import requests 
import bs4
class Duckduckgo():
    def __init__(self):
        """_summary_
        """
        print('search engine : DuckDuckGo')
        self.url = 'https://html.duckduckgo.com/html/'
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        self.httpallowed=True
        self.results = []
        self.payload={}
    def search(self, query, num_pages=1):
        all_links = []
        for page in range(1, num_pages + 1):
            url = f'{self.base_url}{query}&page={page}'
            response = self.session.get(url, headers=self.headers)
            if response.status_code == 200:
                self.results.append(response.text)
                soup = BeautifulSoup(response.text, 'html.parser')
                links = [i.get('href') for i in soup.find_all('a')]
                links = self.cleanlinks(links)
                all_links.extend(links)
            else:
                print(f"Failed to retrieve results for page {page}")

        return all_links
    
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