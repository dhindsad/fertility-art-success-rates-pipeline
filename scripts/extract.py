import pandas as pd
from pathlib import Path

# Get project base directory
BASE_DIR = Path(__file__).resolve().parents[1]

# Create raw data folder
RAW_DIR = BASE_DIR / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)

# Dataset URL (CDC fertility data)
url = "https://data.cdc.gov/api/views/ui6g-vumy/rows.csv?accessType=DOWNLOAD"

# Load data
df = pd.read_csv(url)

# Save raw data
output_file = RAW_DIR / "fertility_raw_data.csv"
df.to_csv(output_file, index=False)

print("Fertility data extracted successfully!")
print(df.head())
print(df.shape)