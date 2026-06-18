from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Open page
    driver.get("https://data.gov.in/catalogs")

    print("Waiting for page to load...")
    time.sleep(10)

    # Get all divs
    divs = driver.find_elements(By.TAG_NAME, "div")

    print(f"\nTotal DIVs Found: {len(divs)}")

    found = False

    for i, div in enumerate(divs):

        try:
            text = div.text.strip()

            if "Road Accidents in India 2022" in text:

                print("\n" + "=" * 80)
                print(f"FOUND AT DIV: {i}")
                print("=" * 80)

                print("\nTEXT INSIDE DIV:\n")
                print(text[:1000])

                print("\n" + "=" * 80)
                print("HTML OF DIV")
                print("=" * 80)

                html = div.get_attribute("outerHTML")

                # Show only first 1000 characters
                print(html[:1000])

                found = True
                break

        except Exception:
            pass

    if not found:
        print("\nCould not find the catalog card.")

    input("\nPress Enter to close...")

finally:
    driver.quit()