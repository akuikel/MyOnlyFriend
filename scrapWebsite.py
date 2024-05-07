from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://chat.openai.com")
time.sleep(10)

driver.quit()