# [Cookie Cutter](https://orteil.dashnet.org/cookieclicker/) Game Auto Bot

# Requirements: [Selenium](https://selenium-python.readthedocs.io) & [Python](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi9y5TW7JGGAxXOHzQIHYSgCKAQFnoECAcQAQ&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&usg=AOvVaw3VuYRIaaa-SL5nRa6pfny0&opi=89978449)

# [Web Scraping & Automation 101 Slides](https://docs.google.com/presentation/d/1dv-s4nqhMxz2rXh_D5vIgXpTvoSy17N227hQoBwml9s/edit?usp=sharing)

___

## Boiler Plate For Self Future Reference

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https://example.com")
```

___

# Get Started 🚩

## 1. Create a Virtual Environment to Containerize your depedencies

For Windows:
```bash
python -m venv myenv
```

For MacOS / Linux:
```bash
python3 -m venv myenv
```

### This tells python to create a venv (virtual environment) with the name "myenv", using the module flag (-m)  

## 2. Then Activate your Virtual Environment

For Windows:
```bash
myenv/Scripts/activate
```

For MacOS / Linux:
```bash
source myenv/bin/activate
```

Your terminal should look like
```bash
(venv) PS D:\...\CookieClickerBot>
```

## 3. Install packages

```bash
pip install -r requirements.txt
```

When installed, to run the program, do

```bash
python YOUR_PYTHON_SCRIPT.py
```

P.S. If your code editor is still showing dependency issues, change your interpreter to the virtual environment you created, ignore this if your imports are working fine :)