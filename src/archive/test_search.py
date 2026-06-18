import requests

url = (
    "https://www.data.gov.in/backend/dmspublic/v1/catalogs"
    "?offset=0"
    "&limit=10"
    "&query=uttar"
)

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)

try:
    data = r.json()
    print("ROWS:", len(data["data"]["rows"]))

    for row in data["data"]["rows"]:
        print(row.get("title", [""])[0])

except Exception as e:
    print(e)