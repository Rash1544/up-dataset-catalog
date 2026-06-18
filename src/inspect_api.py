import requests
import json

url = "https://www.data.gov.in/backend/dmspublic/v1/catalogs?offset=0&limit=1"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

data = r.json()

row = data["data"]["rows"][0]

print("\nAVAILABLE FIELDS:\n")

for key in row.keys():
    print(key)

print("\nFULL RECORD:\n")

print(json.dumps(row, indent=2))