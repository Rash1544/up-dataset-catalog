import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# --------------------------------------------------
# Create outputs folder
# --------------------------------------------------

Path("outputs").mkdir(exist_ok=True)

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

df = pd.read_csv("data/processed/up_dataset_catalog.csv")

print(f"Total Records: {len(df)}")

# --------------------------------------------------
# 1. Top Organisations
# --------------------------------------------------

if "organization" in df.columns:

    org_counts = (
        df["organization"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    org_counts.plot(kind="bar")

    plt.title("Top 10 Organisations")
    plt.ylabel("Number of Datasets")
    plt.tight_layout()

    plt.savefig("outputs/top_organisations.png")
    plt.close()

    print("Saved: outputs/top_organisations.png")

# --------------------------------------------------
# 2. Sector Distribution
# --------------------------------------------------

if "sector" in df.columns:

    sector_counts = (
        df["sector"]
        .fillna("Unknown")
        .value_counts()
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sector_counts.plot(kind="bar")

    plt.title("Top Sectors")
    plt.ylabel("Number of Datasets")

    plt.tight_layout()

    plt.savefig("outputs/sector_distribution.png")
    plt.close()

    print("Saved: outputs/sector_distribution.png")

# --------------------------------------------------
# 3. Format Distribution
# --------------------------------------------------

if "formats" in df.columns:

    all_formats = []

    for item in df["formats"].fillna(""):

        for fmt in str(item).split("|"):

            fmt = fmt.strip()

            if fmt:
                all_formats.append(fmt)

    if len(all_formats) > 0:

        format_counts = (
            pd.Series(all_formats)
            .value_counts()
            .head(10)
        )

        plt.figure(figsize=(10, 6))
        format_counts.plot(kind="bar")

        plt.title("Dataset Formats")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig("outputs/format_distribution.png")
        plt.close()

        print("Saved: outputs/format_distribution.png")

# --------------------------------------------------
# 4. Data Freshness
# --------------------------------------------------

if "metadata_modified" in df.columns:

    dates = pd.to_datetime(
        df["metadata_modified"],
        errors="coerce"
    )

    years = dates.dt.year.dropna()

    if len(years) > 0:

        plt.figure(figsize=(10, 6))

        years.value_counts() \
            .sort_index() \
            .plot(kind="bar")

        plt.title("Dataset Last Updated by Year")
        plt.ylabel("Datasets")

        plt.tight_layout()

        plt.savefig("outputs/data_freshness.png")
        plt.close()

        print("Saved: outputs/data_freshness.png")

# --------------------------------------------------
# 5. Top Tags
# --------------------------------------------------

if "tags" in df.columns:

    tags_list = []

    for item in df["tags"].fillna(""):

        for tag in str(item).split("|"):

            tag = tag.strip()

            if tag:
                tags_list.append(tag)

    if len(tags_list) > 0:

        tag_counts = (
            pd.Series(tags_list)
            .value_counts()
            .head(15)
        )

        plt.figure(figsize=(12, 6))

        tag_counts.plot(kind="bar")

        plt.title("Top Tags")
        plt.ylabel("Count")

        plt.tight_layout()

        plt.savefig("outputs/top_tags.png")
        plt.close()

        print("Saved: outputs/top_tags.png")

# --------------------------------------------------
# 6. Description Quality
# --------------------------------------------------

if "description" in df.columns:

    lengths = (
        df["description"]
        .fillna("")
        .astype(str)
        .str.len()
    )

    plt.figure(figsize=(10, 6))

    lengths.hist(bins=20)

    plt.title("Description Length Distribution")
    plt.xlabel("Characters")
    plt.ylabel("Datasets")

    plt.tight_layout()

    plt.savefig("outputs/description_quality.png")
    plt.close()

    print("Saved: outputs/description_quality.png")

# --------------------------------------------------
# Summary Statistics
# --------------------------------------------------

print("\n========== SUMMARY ==========")

if "organization" in df.columns:
    print(
        "\nTop Organisation:"
    )
    print(
        df["organization"]
        .fillna("Unknown")
        .value_counts()
        .head(5)
    )

if "sector" in df.columns:
    print(
        "\nTop Sector:"
    )
    print(
        df["sector"]
        .fillna("Unknown")
        .value_counts()
        .head(5)
    )

print("\nAnalysis Complete")