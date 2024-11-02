# 5. Dynamic Content Scraping Using Selenium --- Jahnavi
# Objective: Scrape content that loads dynamically via JavaScript, such as infinite
# scrolling pages.
# Data Types: Text, potentially URLs or images.
# Approach:
# Use Selenium to load the page and scroll until all items are visible.
# Extract data by parsing HTML after the content has loaded.
# Example Site: Twitter feed, Medium articles, or any other infinite-scrolling page.

import selenium
from selenium import webdriver
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://in.tradingview.com/chart/?symbol=CRYPTO%3ABTCUSD")

time.sleep(10)

values = driver.find_element(By.CLASS_NAME,value = "priceWrapper-qWcO4bp9")

time.sleep(10)
list1 = []

print(values)



