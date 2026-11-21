# CleanAir India - Air Quality Analytics

## Project objective
Analyse air-quality data for selected Indian cities, compare average AQI,
identify monthly patterns, and communicate findings through charts.

## Included files
- `main.py`: Python analysis script
- `data/air_quality_demo.csv`: small illustrative dataset for testing
- `outputs/`: generated charts and summary CSV files (created after running)

## Important data note
The included AQI values are **illustrative demo values**, not official CPCB readings.
Do not present them as real measurements. For a final submission, replace the CSV
with verified observations from CPCB or data.gov.in and record the source,
date range, units, and any missing-data handling.

## How to run
1. Install Python 3.
2. Open a terminal in this project folder.
3. Install packages:
   `python -m pip install pandas matplotlib`
4. Run:
   `python main.py`

## Expected analysis
- Preview and basic summary of the dataset
- Average AQI by city
- City with the highest average AQI in the dataset
- Average AQI by month
- Bar chart comparing cities
- Line chart showing monthly trend

## Suggested presentation sections
1. Introduction and problem statement
2. Data source and dataset description
3. Data cleaning
4. Analysis questions
5. Charts and observations
6. Limitations
7. Practical awareness recommendations

## Important interpretation note
AQI is a summary indicator. This beginner project compares AQI values only.
It does not prove why pollution levels changed or establish health effects.
