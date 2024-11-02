from selenium import webdriver
from fastapi import FastAPI, HTTPException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

app = FastAPI()


@app.get("/")
def get_stocks():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    driver.get('https://finviz.com/')
    time.sleep(1)

    stocks_data = []

    last_height = driver.execute_script("return document.body.scrollHeight")

    try:
        while True:
            # Find table and rows
            try:
                table = driver.find_element(By.ID, 'js-signals_1')
                rows = table.find_elements(By.TAG_NAME, 'tr')
            except Exception as e:
                raise HTTPException(status_code=500, detail="Error finding table or rows.")

            # Scrape the rows (skip the header row)
            for row in rows[1:]:
                cells = row.find_elements(By.TAG_NAME, 'td')
                if len(cells) > 1:
                    company = cells[0].text.strip()
                    price = cells[1].text.strip()
                    change = cells[2].text.strip()
                    volume = cells[3].text.strip()

                    stocks_data.append({
                        "Company": company,
                        "Price": price,
                        "Change": change,
                        "Volume": volume
                    })

            # Scroll down and wait
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Calculate new scroll height after scrolling
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:  # Break the loop if no new data is loaded
                break
            last_height = new_height

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error scraping stock data")
    finally:
        driver.quit()

    return stocks_data
