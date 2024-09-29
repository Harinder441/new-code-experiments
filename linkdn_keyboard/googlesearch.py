import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

URL = "https://www.google.com/"


class Google:
    def __init__(self):
        service = Service("C:/Development/chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(URL)

    def search(self, q="facebook",firstnresults = 1):
        search_input = self.driver.find_element(By.NAME, "q")
        search_input.clear()
        search_input.send_keys(q)
        search_input.send_keys(Keys.ENTER)
        time.sleep(2)
        # print("hey")
        results =[]
        for i in range(1,firstnresults+1):
            result_xpath = f'//*[@id="rso"]/div[{i}]/div/div/div/div/div/div/div[1]/a'
            try:
                result = self.driver.find_element(By.XPATH, result_xpath)
            except:
                continue
            else:
                results.append(result.get_attribute("href"))

        return results
# /html/body/div[7]/div/div[13]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/div/cite

if __name__ == "__main__":
    g = Google()
    time.sleep(1)
    r=g.search()
    print(r)
    time.sleep(20)
