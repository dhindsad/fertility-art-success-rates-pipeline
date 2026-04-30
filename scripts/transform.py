import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

raw_file = BASE_DIR / "data" / "raw" / "fertility_raw_data.csv"
processed_file = BASE_DIR / "data" / "processed" / "clean_fertility_data.csv"

processed_file.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(raw_file)

print("Raw columns found:")
print(df.columns.tolist())
print("Raw shape:", df.shape)

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
    .str.replace("/", "_")
    .str.replace("(", "", regex=False)
    .str.replace(")", "", regex=False)
)

df = df.drop_duplicates()
df = df.fillna("Unknown")

df.to_csv(processed_file, index=False)

print("Clean file saved.")
print("Clean columns saved:")
print(df.columns.tolist())
print("Clean shape:", df.shape)