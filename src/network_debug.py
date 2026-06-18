from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    def handle_response(response):
        url = response.url

        if "catalog" in url.lower() or "api" in url.lower():
            print("\nURL:")
            print(url)

    page.on("response", handle_response)

    page.goto(
        "https://www.data.gov.in/catalogs",
        wait_until="networkidle"
    )

    input("\nPress Enter...")