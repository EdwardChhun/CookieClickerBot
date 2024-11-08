# pip install selenium

from selenium import webdriver     
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()         # or webdriver.Firefox()

driver.get("https://selenium.dev/selenium/web/mouse_interaction.html")   # Opens a website "Create a new session"              

time.sleep(2)
draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
start = draggable.location
print("Draggable Coords: ", start)

time.sleep(2)
droppable = driver.find_element(By.XPATH, "//div[@id='droppable']")
finish = droppable.location
print("Droppable Coords: ", finish)

time.sleep(2)
ActionChains(driver)\
    .drag_and_drop_by_offset(draggable, finish['x'] - start['x'], finish['y'] - start['y'])\
    .perform()
    
'''
NOTE: Can also be done without using offset:
'''
# draggable = driver.find_element(By.ID, "draggable")
# droppable = driver.find_element(By.ID, "droppable")
# ActionChains(driver) \
#     .drag_and_drop(draggable, droppable) \
#     .perform()


time.sleep(10)
driver.quit()                       # End the session
