from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://data.gov.in/catalogs")

    time.sleep(10)

    print("\nTOTAL LINKS FOUND:", len(driver.find_elements(By.TAG_NAME, "a")))

    links = driver.find_elements(By.TAG_NAME, "a")

    for i, link in enumerate(links):

        text = link.text.strip()

        if text:

            if (
                "Road Accidents" in text
                or "Labour Welfare" in text
                or "Springs" in text
            ):
                print("\n" + "=" * 80)
                print("LINK NUMBER:", i)
                print("=" * 80)

                print("TEXT:")
                print(text)

                print("\nHREF:")
                print(link.get_attribute("href"))

                print("\nCLASS:")
                print(link.get_attribute("class"))

                print("\nOUTER HTML:")
                print(link.get_attribute("outerHTML")[:1000])

    input("\nPress Enter...")

finally:
    driver.quit()