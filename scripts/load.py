import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

processed_file = BASE_DIR / "data" / "processed" / "clean_fertility_data.csv"
database_file = BASE_DIR / "outputs" / "fertility_database.db"
summary_file = BASE_DIR / "outputs" / "fertility_summary_report.csv"

# Create outputs folder if missing
database_file.parent.mkdir(parents=True, exist_ok=True)

# Load cleaned data
df = pd.read_csv(processed_file)

# Save to SQLite database
conn = sqlite3.connect(database_file)
df.to_sql("fertility_success_rates", conn, if_exists="replace", index=False)

# Create simple summary report
summary = pd.DataFrame({
    "total_rows": [len(df)],
    "total_columns": [len(df.columns)],
    "duplicate_rows": [df.duplicated().sum()]
})

summary.to_csv(summary_file, index=False)

conn.close()

print("Fertility data loaded successfully!")
print("Database created:", database_file)
print("Summary report created:", summary_file)
print(summary)