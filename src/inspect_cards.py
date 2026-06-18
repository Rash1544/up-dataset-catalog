from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install())
)

driver.get("https://data.gov.in/catalogs")

time.sleep(5)

cards = driver.find_elements(By.CSS_SELECTOR, "div.catalog-item")

print("Cards Found:", len(cards))

for i, card in enumerate(cards[:3]):
    print("\n" + "="*50)
    print("CARD", i+1)
    print("="*50)

    print(card.get_attribute("outerHTML")[:3000])

input("Press Enter to close...")
driver.quit()