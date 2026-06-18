import requests
import json
import os
import time

BASE_URL = "https://www.data.gov.in/backend/dmspublic/v1/catalogs"

os.makedirs("data/raw", exist_ok=True)

offset = 0
limit = 100
page = 1
total_records = 0

while True:

    url = (
        f"{BASE_URL}"
        f"?offset={offset}"
        f"&limit={limit}"
        f"&query=uttar pradesh"
    )

    print(f"Fetching page {page}")

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    data = response.json()

    rows = data["data"]["rows"]

    if len(rows) == 0:
        break

    filename = f"data/raw/page_{page:03d}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    total_records += len(rows)

    print(
        f"Saved {filename} | "
        f"records={len(rows)} | "
        f"total={total_records}"
    )

    offset += limit
    page += 1

    time.sleep(1)

print()
print("TOTAL RECORDS:", total_records)