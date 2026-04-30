# Fertility Data Pipeline & Healthcare Analytics Dashboard

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python to process and analyze fertility clinic data from publicly available ART datasets.

The goal of this project is to simulate real-world healthcare data workflows and generate insights related to clinic activity, treatment volume, and operational trends.

## Tools & Technologies
- Python (Pandas)
- SQLite (Database)
- Tableau (Data Visualization)

## Pipeline Architecture
Extract → Transform → Validate → Load → Dashboard

## Workflow

### 1. Extract
- Retrieved fertility clinic dataset from public data source
- Loaded raw data into structured format

### 2. Transform
- Cleaned column names and standardized formats
- Handled missing values and corrected data types
- Removed duplicates and prepared data for analysis

### 3. Validate
- Checked for missing values and duplicates
- Ensured data consistency and structure

### 4. Load
- Stored cleaned data into SQLite database
- Generated summary report for analysis

### 5. Visualization
- Created Tableau dashboard to analyze:
  - Clinic distribution by location
  - Treatment activity levels
  - Subtopic-level healthcare insights

## Dashboard

https://public.tableau.com/app/profile/deepanshu.dhindsa/viz/FertilityTreatmentOutcomesandClinicInsights/Dashboard1


## Key Insights
- Fertility clinic activity varies significantly by location
- Treatment volume provides insight into clinic demand and capacity
- Subtopic analysis highlights different healthcare metrics tracked across clinics
- Data cleaning and transformation are critical for accurate healthcare analytics

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
