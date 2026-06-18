import requests

offset = 0
limit = 100

total = 0

while True:

    url = (
        "https://www.data.gov.in/backend/dmspublic/v1/catalogs"
        f"?offset={offset}"
        f"&limit={limit}"
        "&query=uttar pradesh"
    )

    r = requests.get(
        url,
        headers={"User-Agent":"Mozilla/5.0"}
    )

    data = r.json()

    rows = data["data"]["rows"]

    if len(rows) == 0:
        break

    total += len(rows)

    print("Collected:", total)

    offset += limit

print()
print("TOTAL:", total)