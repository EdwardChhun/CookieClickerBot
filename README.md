[Cookie Cutter](https://orteil.dashnet.org/cookieclicker/) Game Auto Bot

Requirements: [Selenium](https://selenium-python.readthedocs.io) & [Python](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi9y5TW7JGGAxXOHzQIHYSgCKAQFnoECAcQAQ&url=https%3A%2F%2Fwww.python.org%2Fdownloads%2F&usg=AOvVaw3VuYRIaaa-SL5nRa6pfny0&opi=89978449)

___

Boiler Plate For Self Future Reference

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
driver = webdriver.Chrome(options=options)

driver.get("https:example.com")
```

___

To install selenium, run in terminal

For Windows:
```bash
pip install selenium
```

For Mac:

```bash
python3 install selenium
```

When installed, to run the program, do

```bash
python cookieclickers.py
```
