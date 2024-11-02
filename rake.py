# from boilerpy3 import extractors

# extractor = extractors.ArticleExtractor()

# # From a URL
# content = extractor.get_content_from_url('http://example.com/')

# # From a file
# content = extractor.get_content_from_file('tests/test.html')

# # From raw HTML
# content = extractor.get_content('<html><body><h1>Example</h1></body></html>')

# from boilerpy3 import extractors
#
# extractor = extractors.KeepEverythingExtractor()
#
# doc = extractor.get_doc_from_url('https://www.hindustantimes.com/india-news/misleading-people-under-guise-of-dravidian-model-actor-turned-politician-vijays-veiled-jibe-at-dmk-101730033694947.html')
# content = doc.content
# title = doc.title
# print(title)
# print(con)
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
df = pd.read_csv('market_prices.csv')

# Convert 'Price' column to numeric (float) to avoid string-related errors
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Filter data by ID for different stocks
sensex_data = df[df['ID'] == 'BSE Sensex'].copy()
crypto_data = df[df['ID'] == 'Crypto BTC'].copy()

# Remove any rows with NaN values in the 'Price' column after conversion
sensex_data = sensex_data.dropna(subset=['Price'])
crypto_data = crypto_data.dropna(subset=['Price'])

# Convert 'Timestamp' column to only show the time as string for x-axis
sensex_data['Time'] = pd.to_datetime(sensex_data['Timestamp']).dt.strftime('%H:%M:%S')
crypto_data['Time'] = pd.to_datetime(crypto_data['Timestamp']).dt.strftime('%H:%M:%S')

# Define dynamic y-axis ranges with a buffer of ±50 around min and max values
sensex_y_min, sensex_y_max = sensex_data['Price'].min() - 50, sensex_data['Price'].max() + 50
crypto_y_min, crypto_y_max = crypto_data['Price'].min() - 50, crypto_data['Price'].max() + 50

# Set up subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))

# Plot BSE Sensex data
ax1.plot(sensex_data['Time'], sensex_data['Price'], color='blue', linestyle='-', linewidth=1.5,
         marker='o', markersize=5, label='BSE Sensex')
ax1.set_title('BSE Sensex Price Over Time')
ax1.set_xlabel('Time')
ax1.set_ylabel('Price')
ax1.set_ylim(sensex_y_min, sensex_y_max)  # Fixed y-axis range based on data
ax1.legend()
ax1.grid(True, which='both', linestyle='--', linewidth=0.5)
ax1.tick_params(axis='x', rotation=45)

# Plot Crypto BTC data
ax2.plot(crypto_data['Time'], crypto_data['Price'], color='red', linestyle='-', linewidth=1.5,
         marker='o', markersize=5, label='Crypto BTC')
ax2.set_title('Crypto BTC Price Over Time')
ax2.set_xlabel('Time')
ax2.set_ylabel('Price (USD)')
ax2.set_ylim(crypto_y_min, crypto_y_max)  # Fixed y-axis range based on data
ax2.legend()
ax2.grid(True, which='both', linestyle='--', linewidth=0.5)
ax2.tick_params(axis='x', rotation=45)

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

