import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_fertility_data.csv"

df = pd.read_csv(processed_file)

print("Running fertility data validation checks...")

# Check 1: Missing values
missing_values = df.isnull().sum()
print("\nMissing values:")
print(missing_values)

# Check 2: Duplicate rows
duplicates = df.duplicated().sum()
print("\nDuplicate rows:", duplicates)

# Check 3: Empty dataset check
row_count = len(df)
column_count = len(df.columns)

print("\nRows:", row_count)
print("Columns:", column_count)

# Check 4: Unknown values count
unknown_count = (df == "Unknown").sum().sum()
print("\nUnknown values:", unknown_count)

if row_count > 0 and column_count > 0 and duplicates == 0:
    print("\nValidation passed. Fertility data is ready for reporting.")
else:
    print("\nValidation completed. Please review issues above.")