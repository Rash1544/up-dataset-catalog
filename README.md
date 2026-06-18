# Government Open Data Catalog Extractor

## Project Overview

This project extracts metadata from India's Open Government Data (OGD) Platform (data.gov.in) using its backend APIs.

The system automatically collects catalog information, validates data quality, and stores the results in structured CSV format for further analytics and research.

---

## Features

- API Discovery using Browser Network Inspection
- Automated Catalog Extraction
- Pagination Handling
- Metadata Collection
- CSV Export
- Data Quality Validation
- Duplicate Detection
- Missing Value Analysis

---

## Dataset Statistics

- Total Records: 12,621
- Missing Values: 0
- Duplicate Records: 0

---

## Tech Stack

- Python
- Requests
- Pandas
- Playwright
- CSV

---

## Project Structure

data/
raw/
processed/

src/
collect_data.py
download_all_catalogs.py
extract_catalogs.py

outputs/

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python src/download_all_catalogs.py
```

---

## Sample Output

- all_catalogs.csv
- catalog_links.csv
- catalogs.csv

---
## Key Findings

1. Health and Family Welfare is the most represented sector with the largest number of published datasets.

2. The Ministry of Health and Family Welfare is the leading contributor of datasets on the platform.

3. Dataset availability is concentrated in a few sectors, while several domains appear underrepresented.

4. Some records contain incomplete organisation metadata, indicating a need for better metadata governance.

5. These insights can help SDA prioritise departmental outreach and improve metadata registry design.

## Author

Rashmi Gulati