from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Function to scroll to the end of the page
def scroll_to_end():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for new content to load
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Function to fetch data from a URL
def fetch_price(url, price_selector, record_id):
    driver.get(url)
    scroll_to_end()  # Scroll to the end of the page to load all content

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Wait for the price element to load dynamically
        price_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, price_selector))
        )
        price = price_element.text
        print(f"ID: {record_id} | Timestamp: {timestamp} | Price: {price}")
        return [record_id, timestamp, price]
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")
        return [record_id, timestamp, None]

# Function to save data to CSV and plot graphs
def save_and_plot(all_data):
        df = pd.DataFrame(all_data, columns=['ID', 'Timestamp', 'Price'])
        df.to_csv('market_prices.csv', index=False)

        df['Time'] = pd.to_datetime(df['Timestamp']).dt.time
        # Separate data by ID
        sensex_data = df[df['ID'] == 'BSE Sensex']
        crypto_data = df[df['ID'] == 'Crypto BTC']

        # Plotting
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

        ax1.plot(sensex_data['Time'], sensex_data['Price'], marker='o', linestyle='-', color='b',
                 label='BSE Sensex')
        ax1.set_title('BSE Sensex Price Over Time')
        ax1.set_xlabel('Time')
        ax1.set_ylabel('Price')
        ax1.legend()


        ax2.plot(crypto_data['Time'], crypto_data['Price'], marker='o', linestyle='-', color='r',
                 label='Crypto BTC')
        ax2.set_title('Crypto BTC Price Over Time')
        ax2.set_xlabel('Time')
        ax2.set_ylabel('Price')
        ax2.legend()


        plt.tight_layout()
        plt.show()

# Main loop to fetch and save data every 2 minutes
def main():
    websites = [
        {"url": "https://www.bseindia.com/sensex/code/16/", "selector": "viewsensexvalue", "name": "BSE Sensex"},
        {"url": "https://in.tradingview.com/chart/?symbol=CRYPTO%3ABTCUSD", "selector": "priceWrapper-qWcO4bp9", "name": "Crypto BTC"},
    ]
    all_data = []

    try:
        while True:
            for website in websites:
                data = fetch_price(website["url"], website["selector"], website["name"])
                all_data.append(data)

            print("Data saved and plotted. Waiting for 2 minutes...")
            time.sleep(30)

    except KeyboardInterrupt:
        print("Script stopped manually.")
    finally:
        driver.quit()
        save_and_plot(all_data)
# Run the main function
if __name__ == "__main__":
    main()
