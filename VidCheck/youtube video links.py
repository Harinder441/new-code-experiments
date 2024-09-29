from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
playlist_url = "https://youtube.com/playlist?list=PL3DxmzKXBoQ6rqvCu6LIKtEiBYKanjZKK"
driver = webdriver.Chrome()
driver.get(playlist_url)
time.sleep(10)
wait = WebDriverWait(driver, 20)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-playlist-video-renderer #video-title")))
anchor_tags = driver.find_elements(By.CSS_SELECTOR, "ytd-playlist-video-renderer #video-title")

with open("Diksha.txt","w") as file:
    for i in range(len(anchor_tags)):
        file.write(f"{anchor_tags[i].get_attribute('title')} \n { anchor_tags[i].get_attribute('href')} \n\n ")


driver.quit()
