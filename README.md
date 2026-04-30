# Fertility Data Pipeline & Outcomes Dashboard

## Overview
This project demonstrates an end-to-end healthcare data pipeline using Python to process fertility treatment data.

The pipeline extracts publicly available ART fertility data, cleans and transforms it, validates data quality, loads it into a SQLite database, and prepares outputs for reporting and visualization.

## Tools Used
- Python
- Pandas
- SQLite
- Tableau

## Pipeline Architecture
Extract → Transform → Validate → Load → Dashboard

## Project Structure
```text
fertility-data-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── scripts/
├── outputs/
├── notebooks/
└── README.md