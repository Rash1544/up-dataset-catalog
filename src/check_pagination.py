from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto(
        "https://www.data.gov.in/catalogs",
        wait_until="networkidle"
    )

    print("\nALL LINKS:\n")

    links = page.locator("a").all()

    for i, link in enumerate(links):
        try:
            text = link.inner_text().strip()
            href = link.get_attribute("href")

            if text:
                print(f"{i}: {text} -> {href}")

        except:
            pass

    input("\nPress Enter...")