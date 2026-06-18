import requests
import pandas as pd
import time

BASE_URL = "https://www.data.gov.in/backend/dmspublic/v1/catalogs"

all_rows = []

offset = 0
limit = 100   # Fetch 100 records at a time

while True:

    url = (
        f"{BASE_URL}"
        f"?offset={offset}"
        f"&limit={limit}"
        f"&sort[published_date]=desc"
    )

    print(f"Fetching offset={offset}")

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    data = response.json()

    rows = data["data"]["rows"]

    if len(rows) == 0:
        break

    for row in rows:

        title = ""

        if "title" in row:
            title = row["title"][0]

        description = ""

        if "body:value" in row:
            description = row["body:value"][0]

        catalog_url = ""

        if "node_alias" in row:
            catalog_url = (
                "https://www.data.gov.in"
                + row["node_alias"][0]
            )

        all_rows.append({
            "title": title,
            "url": catalog_url,
            "description": description
        })

    offset += limit

    time.sleep(1)

df = pd.DataFrame(all_rows)

print("\nTOTAL RECORDS:")
print(len(df))

df.to_csv(
    "all_catalogs.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nSaved as all_catalogs.csv")