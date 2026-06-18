import json
import pandas as pd
from pathlib import Path

raw_folder = Path("data/raw")

records = []

for file in raw_folder.glob("page_*.json"):

    print("Reading:", file)

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    rows = data["data"]["rows"]

    for row in rows:

        records.append({

            "dataset_id":
                row.get("uuid", [""])[0],

            "title":
                row.get("title", [""])[0].strip(),

            "organization":
                row.get(
                    "field_ministry_department:name",
                    [""]
                )[0].strip(),

            "sector":
                row.get(
                    "field_sector:name",
                    [""]
                )[0].strip(),

            "tags":
                "|".join(
                    row.get("keywords", [])
                ),

            "formats":
                "",

            "num_resources":
                "",

            "metadata_created":
                row.get("created", [""])[0],

            "metadata_modified":
                row.get("changed", [""])[0],

            "description":
                row.get(
                    "body:value",
                    [""]
                )[0].strip(),

            "source_url":
                "https://www.data.gov.in"
                + row.get(
                    "node_alias",
                    [""]
                )[0]

        })

df = pd.DataFrame(records)

print()
print("Records before dedupe:", len(df))

df = df.drop_duplicates(
    subset=["dataset_id"]
)

print("Records after dedupe:", len(df))

processed_dir = Path("data/processed")
processed_dir.mkdir(
    parents=True,
    exist_ok=True
)

output_file = (
    processed_dir
    / "up_dataset_catalog.csv"
)

df.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print()
print("Saved:", output_file)