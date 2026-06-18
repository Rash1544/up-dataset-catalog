import requests

url = "https://www.data.gov.in/catalogs"

response = requests.get(url)

html = response.text

# save page
with open("catalog_page.html", "w", encoding="utf-8") as f:
    f.write(html)

print("HTML saved successfully")