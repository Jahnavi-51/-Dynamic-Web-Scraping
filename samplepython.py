from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pandas as pd

# Set up Selenium WebDriver
driver = webdriver.Chrome()


def scrape_infinite_scroll(url):
    driver.get(url)

    # Allow time for the initial content to load
    time.sleep(2)

    # Get the initial height of the page
    last_height = driver.execute_script("return document.body.scrollHeight")

    list1 = []
    while True:
        # Scroll down to the bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait for new content to load
        time.sleep(2)

        # Calculate new scroll height and compare it with the last height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # Break the loop if no new content is loaded
        last_height = new_height

    # After scrolling, extract the desired content
    elements = driver.find_elements(By.CLASS_NAME,
                                            'priceWrapper-qWcO4bp9')  # Adjust the XPath as needed
    name = driver.find_element(By.CSS_SELECTOR, "span[data-name='details-exchange']")
    n = name.text
    # names = driver.find_element(By.XPATH,"//div[contains(@class,'item-JLr4OyLc')]")

    for element in elements:
        print(n)
        e = element.text
        print(e)  # Extract and print the text or other attribute
        d = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("time :",d)

        list1.append([n,e,d])

    df = pd.DataFrame(list1, columns=['Name','Price', 'Time'])
    df.to_csv
# URL of the infinite scrolling page (e.g., Twitter feed, Medium articles)
url = "https://in.tradingview.com/chart/?symbol=CRYPTO%3ABTCUSD " # Replace with the actual URL
scrape_infinite_scroll(url)

# Close the WebDriver
driver.quit()



