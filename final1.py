from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd
from matplotlib import pyplot as plt

# Set up Selenium WebDriver
driver = webdriver.Chrome()


# Function to fetch data from a URL
def fetch_price(url, price_selector, record_id):
    driver.get(url)

    # Initialize timestamp to ensure it's always defined
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Wait for the price element to load dynamically
        price_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, price_selector))
            # Ensure you're using the correct selector
        )
        price = price_element.text

        print(f"ID: {record_id} | Timestamp: {timestamp} | Price: {price}")
        return [record_id, timestamp, price]

    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return [record_id, timestamp, None]  # Return None if there's an error


# Main loop to fetch and save data every 2 minutes
def main():
    # URLs and selectors for both websites
    websites = [
        {"url": "https://www.bseindia.com/sensex/code/16/", "selector": "viewsensexvalue", "name": "BSE Sensex"},
        {"url": "https://in.tradingview.com/chart/?symbol=CRYPTO%3ABTCUSD", "selector": "priceWrapper-qWcO4bp9",
         "name": "Crypto BTC"},
    ]

    all_data = []

    try:
        while True:  # Run indefinitely
            for website in websites:
                # Fetch new data from each website
                data = fetch_price(website["url"], website["selector"], website["name"])
                all_data.append(data)  # Add the new data to the list

                # Save to CSV
                df = pd.DataFrame(all_data, columns=['ID', 'Timestamp', 'Price'])
                df.to_csv('market_prices.csv', index=False)
                time.sleep(20)

            print("Data saved. Waiting for 2 minutes...")
            time.sleep(30)  # Wait 2 minutes before the next fetch

    except KeyboardInterrupt:
        print("Script stopped manually.")
    finally:
        driver.quit()  # Ensure the driver is closed

# Run the main function
if __name__ == "__main__":
    main()
