from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import os

os.makedirs("data/raw", exist_ok=True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://www.data.gov.in/catalogs")

time.sleep(10)

page_text = driver.find_element("tag name", "body").text

with open("data/raw/page_001.txt", "w", encoding="utf-8") as f:
    f.write(page_text)

print("Page saved successfully!")

driver.quit()