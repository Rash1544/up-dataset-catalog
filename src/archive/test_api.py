import requests

url = "https://www.data.gov.in/backend/dmspublic/v1/catalogs?offset=0&limit=8&sort[published_date]=desc"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("content-type"))
print()
print(r.text[:1000])