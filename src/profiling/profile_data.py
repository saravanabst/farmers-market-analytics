from pathlib import Path
import pandas as pd

# -----------------------------
# Project Paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
REPORT_PATH = PROJECT_ROOT / "reports"

REPORT_PATH.mkdir(exist_ok=True)

summary = []

print("=" * 60)
print(" FARMERS MARKET DATA PROFILING ")
print("=" * 60)

# Read every CSV
for csv_file in RAW_DATA_PATH.glob("*.csv"):

    print(f"\nReading: {csv_file.name}")

    df = pd.read_csv(csv_file)

    rows = len(df)
    cols = len(df.columns)
    duplicates = df.duplicated().sum()
    missing = df.isnull().sum().sum()

    summary.append({
        "File": csv_file.name,
        "Rows": rows,
        "Columns": cols,
        "Duplicate Rows": duplicates,
        "Missing Values": missing
    })

    print(f"Rows           : {rows}")
    print(f"Columns        : {cols}")
    print(f"Duplicates     : {duplicates}")
    print(f"Missing Values : {missing}")

summary_df = pd.DataFrame(summary)

output_file = REPORT_PATH / "data_profile_summary.csv"
summary_df.to_csv(output_file, index=False)

print("\n")
print("=" * 60)
print("Data Profiling Completed Successfully")
print(f"Report saved to: {output_file}")
print("=" * 60)