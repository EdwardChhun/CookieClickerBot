from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://www.selenium.dev/selenium/web/inputs.html")

driver.find_element(By.NAME, "color_input").click()

