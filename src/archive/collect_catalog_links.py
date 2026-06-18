# src/collect_catalog_links.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:

    driver.get("https://www.data.gov.in/catalogs")

    time.sleep(10)

    links = driver.find_elements(By.TAG_NAME, "a")

    catalogs = []

    for link in links:

        href = link.get_attribute("href")
        text = link.text.strip()

        if href and "/catalog/" in href:

            catalogs.append({
                "title": text,
                "url": href
            })

    df = pd.DataFrame(catalogs)

    df = df.drop_duplicates()

    print(df.head())

    print("\nTOTAL CATALOGS FOUND:")
    print(len(df))

    df.to_csv(
        "data/processed/catalog_links.csv",
        index=False
    )

    print("\nSaved Successfully!")

finally:
    driver.quit()