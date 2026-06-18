# UP Dataset Catalog Analysis for State Data Authority (SDA)

## Project Overview

This project was developed as part of the SDA Metadata Registry assignment.

The objective was to collect, clean, and analyse Uttar Pradesh related datasets published on India's Open Government Data (OGD) Platform (data.gov.in). The project helps SDA understand existing public data availability, metadata quality, and sector-wise coverage before departments formally register datasets into the UP Metadata Registry.

---

## Data Collection Approach

The data was collected using the data.gov.in backend catalog API.

Pagination was implemented to retrieve all available Uttar Pradesh related datasets.

Collected records were stored as raw JSON files in the `data/raw/` directory to preserve the original source data.

### Data Source

https://data.gov.in

### Records Collected

* Total UP-related datasets collected: 164

---

## Repository Structure

up-dataset-catalog/

├── src/
│   ├── collect_data.py
│   ├── consolidate_data.py
│   └── analyse.py
│
├── data/
│   ├── raw/
│   └── processed/
│       └── up_dataset_catalog.csv
│
├── outputs/
│   ├── top_organisations.png
│   ├── sector_distribution.png
│   ├── data_freshness.png
│   ├── top_tags.png
│   └── description_quality.png
│
├── README.md
└── requirements.txt

---

## Data Consolidation & Transformation

The consolidation step reads all raw JSON files and converts them into a single analysis-ready dataset.

### Standardisation Performed

* Converted column names to snake_case
* Removed duplicate records using dataset_id
* Converted dates into standard format
* Stored tags and formats as pipe-separated values
* Trimmed whitespace from text fields

### Missing Value Handling

Missing values were filled with "Unknown" where appropriate to preserve records and maintain consistency during analysis.

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Collect data:

```bash
python src/collect_data.py
```

Consolidate data:

```bash
python src/consolidate_data.py
```

Run analysis:

```bash
python src/analyse.py
```

---

## Analysis & Insights

The following visualisations are generated:

* Top Organisations
* Sector Distribution
* Data Freshness
* Top Tags
* Description Quality

Charts are saved in the `outputs/` directory.

---

## Key Findings

1. Health and Family Welfare is the most represented sector among Uttar Pradesh related datasets.

2. Ministry of Health and Family Welfare contributes the highest number of datasets.

3. Dataset coverage is concentrated in a small number of sectors, indicating potential gaps in registry participation.

4. Several datasets contain incomplete organisation metadata, highlighting opportunities for metadata standardisation.

5. Most datasets contain useful descriptions, although metadata quality varies across publishers.

---

## Challenges & Limitations

* Some datasets contained incomplete metadata fields.
* Organisation information was missing for several records.
* Not all records exposed identical metadata attributes through the public API.

---

## Technologies Used

* Python
* Requests
* Pandas
* Matplotlib

---

## Author

Rashmi Gulati
