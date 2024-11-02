from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from datetime import datetime
import pandas as pd


# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Function to fetch data from Crypto URL
def fetch_crypto_price(url, price_selector):
    driver.get(url)
    time.sleep(10)  # Wait for the page to load

    # Extract price
    price_element = driver.find_element(By.CLASS_NAME, price_selector)
    price = price_element.text

    # Generate timestamp and unique ID
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record_id = "Crypto" # Generate a unique ID

    print(f"ID: {record_id} | Timestamp: {timestamp} | Price: {price}")
    return [record_id, timestamp, price]

# Main loop to fetch and save data every 2 minutes
def main():

    url = "https://in.tradingview.com/chart/?symbol=CRYPTO%3ABTCUSD"
    # url ="https://www.bseindia.com/sensex/code/16/"
    price_selector = 'viewsensexvalue'
    price_selector = 'highlight-maJ2WnzA highlight-BSF4XTsE price-qWcO4bp9"'
    # price_selector = 'priceWrapper-qWcO4bp9'# Adjust based on site structure
    all_data = []

    try:
        while True:  # Run indefinitely
            # Fetch new data
            data = fetch_crypto_price(url, price_selector)
            all_data.append(data)  # Add the new data to the list

            # Save to CSV
            df = pd.DataFrame(all_data, columns=['ID', 'Timestamp', 'Price'])
            df.to_csv('crypto_prices.csv', index=False)

            print("Data saved. Waiting for 2 minutes...")
            time.sleep(5)  # Wait 5 seconds before the next fetch

    except KeyboardInterrupt:
        print("Script stopped manually.")
    finally:
        driver.quit()  # Ensure the driver is closed

# Run the main function
if __name__ == "__main__":
    main()

