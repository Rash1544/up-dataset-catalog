import re

with open("data/raw/page_001.txt", "r", encoding="utf-8") as f:
    text = f.read()

matches = re.findall(
    r"(.*?)\nCatalog API\nZip Download\nShare",
    text,
    re.DOTALL
)

for i, item in enumerate(matches, start=1):
    print("\n" + "="*50)
    print(f"CATALOG {i}")
    print("="*50)
    print(item.strip())