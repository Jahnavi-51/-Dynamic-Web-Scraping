from selenium import webdriver
from selenium.webdriver.common.by import By
# import openpyxl
import pandas as pd
import time

dr = webdriver.Chrome()
dr.get("https://finviz.com/")

# workbook = openpyxl.Workbook()
# sheet = workbook.active
# sheet.title = "StockMarket Extracted data"
# sheet.append(["Names","Subsector","Marketcap"])
time.sleep(5)
tr = dr.find_element()
table = dr.find_element(By.ID,'js-signals_1')

rows = table.find_elements(By.CLASS_NAME, 'tr')

list1 = []

for row in rows[1:]:
    cells = row.find_elements(By.TAG_NAME,'td')
    if len(cells) > 1 :
            try :
                company = cells[0].text
                price = cells[1].text
                change = cells[2].text
                volume = cells[3].text
                list1.append([company,price,change,volume])
            except IndexError:
                continue

dr.quit()

df = pd.DataFrame(list1,columns=['Company','price','change','volume'])

f = "stocksjanu.xlsx"
df.to_excel(f)

print("Sucessuful")