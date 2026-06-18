import requests

url = "https://www.data.gov.in/backend/dmspublic/v1/catalogs?offset=0&limit=100"

r = requests.get(url, headers={"User-Agent":"Mozilla/5.0"})

data = r.json()

for row in data["data"]["rows"]:

    jurisdiction = row.get(
        "field_asset_jurisdiction:name",
        ["Unknown"]
    )[0]

    if "Uttar" in jurisdiction:
        print(jurisdiction)