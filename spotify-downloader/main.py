from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyperclip

playlist_url = "https://open.spotify.com/playlist/43LLJSa09ny8o5ICcK9bUI?si=1feab9badfa54ab7"
pyperclip.copy(playlist_url)

driver = webdriver.Chrome()
driver.get("https://spotifydown.com/")

sleep(5)
# Find the input bar by its ID and fill it with data
input_bar = driver.find_element(By.XPATH,'/html/body/div/div/div[1]/input')
input_bar.click()
input_bar.send_keys(Keys.CONTROL + "v")

input_bar.send_keys(Keys.ENTER)




sleep(5)
# Find all download buttons by XPath
download_buttons = driver.find_elements(By.XPATH,"//button[contains(text(),'Download')]")
print(len(download_buttons))
driver.quit()

for button in download_buttons:
    sleep(2)
    button.click()
    sleep(7)
        #     anchor_tag = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/a[1]')))

    # try:
    anchor_tag = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[1]/a[1]')
    print(anchor_tag.get_attribute("href"))
    sleep(10)
    # except:
    #     print("Failed to download ", button.get_attribute("href"))

# sleep(60)
# Quit the driver

