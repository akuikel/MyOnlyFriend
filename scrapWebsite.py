from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://chat.openai.com")

# Wait for the input box to be present
input_box = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "prompt-textarea"))
)

# Type the prompt into the input box
input_box.send_keys("Hey how are you?")

time.sleep(5)
# Send an "Enter" key press to submit the prompt
input_box.send_keys(Keys.ENTER)
