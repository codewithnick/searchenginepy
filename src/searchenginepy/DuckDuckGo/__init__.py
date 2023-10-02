#Duckduckgo class which has functions to search and get results
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class DuckduckgoScraper:
    def __init__(self):
        self.base_url = 'https://duckduckgo.com/'
        self.driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
        self.results = []

    def search(self, query, num_pages=1):
        self.driver.get(self.base_url)
        search_input = self.driver.find_element(By.NAME, 'q')
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

        for _ in range(num_pages):
            self.scroll_down()
            time.sleep(2)  # You may adjust the delay as needed
            self.click_more_results()

        links = self.extract_links()
        self.driver.quit()
        return links

    def scroll_down(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.END)
        actions.perform()

    def click_more_results(self):
        try:
            more_results_button = self.driver.find_element(By.CLASS_NAME, 'result--more__btn')
            more_results_button.click()
        except Exception as e:
            print(f"Unable to click 'More Results' button: {e}")

    def extract_links(self):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', class_='result__url')]
        return links

# Example usage:
scraper = DuckduckgoScraper()
search_results = scraper.search('your_query_here', num_pages=3)
for link in search_results:
    print(link)