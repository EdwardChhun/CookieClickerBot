from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

url = "https://en.wikipedia.org/wiki/String_theory"
driver.get(url)

time.sleep(0.1)

textbooks_list = driver.find_element(By.XPATH, "//div[@class='mw-content-container']//ul[2]")
textbooks = textbooks_list.find_elements(By.TAG_NAME, "li")

results = []

def scrapeTextbooks():
    
    for i, textbook in enumerate(textbooks): # Creates an ordered pair of (index, value)
        result = ("Textbook " + str(i + 1) + ": " + textbook.text)
        results.append(result)
        print(result)

    
def saveTextbooksToTxt(filename):
    file = open(filename, "w")
    for result in results:
        file.write(result + "\n")
    file.close()

if __name__ == "__main__":
    print("Textbooks for URL: ", url)
    scrapeTextbooks()
    saveTextbooksToTxt("textbooks.txt")
    

