import pandas as pd

with open("data/raw/page_001.txt", "r", encoding="utf-8") as f:
    lines = [x.strip() for x in f.readlines()]

datasets = []

for i, line in enumerate(lines):

    if "Road Accidents" in line or "Census" in line or "Water" in line:

        title = line

        ministry = ""

        description = ""

        for j in range(i+1, min(i+15, len(lines))):

            if (
                "Ministry" in lines[j]
                or "Board" in lines[j]
                or "Department" in lines[j]
            ):
                ministry = lines[j]

                if j+1 < len(lines):
                    description = lines[j+1]

                break

        datasets.append(
            {
                "title": title,
                "ministry": ministry,
                "description": description
            }
        )

df = pd.DataFrame(datasets)

print(df)

df.to_csv(
    "data/processed/catalogs.csv",
    index=False
)

print("\nCSV Saved Successfully!")