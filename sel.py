from selenium import webdriver
#pip install selenium
class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/Anoushka C/OneDrive/Desktop/VS CODE/Automate.py/chromedriver.exe")

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        #for search bar
        search.click()
        search.send_keys(query)
        enter=self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        #for enter button
        enter.click()


#assit=info()
#assit.get_info('hi')