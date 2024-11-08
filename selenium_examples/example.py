from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://google.com")
#-------------------------------------------------
# From here above is the boiler plate for selenium

# Waiting for the element to exist

WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

# Finding then element and then do inputs
input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.clear()
input_element.send_keys("Sacramento City College" + Keys.ENTER)

# Test if links exist
WebDriverWait(driver,5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Sacramento City College"))
)

# Finding the partial link and click on it
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Sacramento City College")

link.click()

time.sleep(10)

driver.quit()