from selenium import webdriver

class music():
    def __init__(self):  #self is a gloabal variabe
        self.driver = webdriver.Chrome(executable_path="D:/Coding/VS CODE/Automate.py/chromedriver.exe")

    def play(self,query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query="+query)
        #we will give the xpath of the first video found on searching for this song
        xpath = '//*[@id="video-title"]/yt-formatted-string'
        video = self.driver.find_element_by_xpath(xpath)
        video.click()



