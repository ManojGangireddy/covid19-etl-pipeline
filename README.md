# COVID-19 ETL Pipeline with Machine Learning

## Overview
This project demonstrates a complete ETL pipeline using Python. It extracts COVID-19 data from a public API, transforms and cleans it, loads it into a PostgreSQL database, and visualizes trends. Additionally, it applies machine learning (KMeans clustering) to group countries by their case and death counts.

## Components
- `extract.py`: Connects to the API and saves raw data as CSV
- `transform.py`: Cleans and structures the raw data
- `load.py`: Loads transformed data into a PostgreSQL database
- `visualize.py`: Generates a bar chart for the top 5 most affected countries
- `cluster.py`: Applies KMeans clustering and produces a scatter plot with labeled country points

## Database Setup
Ensure PostgreSQL is installed and a database named `covid19` is created. Update your credentials in `load.py`.

Example SQL schema (see `database_schema.sql`):
```sql
CREATE TABLE covid_stats (
    country VARCHAR(100),
    cases INTEGER,
    deaths INTEGER,
    recovered INTEGER,
    active INTEGER,
    critical INTEGER,
    casesPerOneMillion FLOAT,
    population BIGINT,
    cluster INTEGER
);
```

## Installation
Create and activate a virtual environment, then install dependencies:
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

## Flowchart
```
[API] → [extract.py] → raw_covid_data.csv
                  ↓
          [transform.py] → clean_covid_data.csv
                           ↓
                   [load.py] → PostgreSQL DB
                                ↓
                         [visualize.py] → top5_countries.png
                                              ↓
                         [cluster.py] → clustering_plot.png
```

## Output
- `raw_covid_data.csv`: Raw JSON data flattened
- `clean_covid_data.csv`: Cleaned data ready for loading
- `top5_countries.png`: Bar chart of top affected countries
- `clustering_plot.png`: Clustering scatter plot using KMeans

## Notes
- Modify database connection strings as needed.
- KMeans can be extended with additional features or dimensionality reduction for deeper insight.
- Set a cron job to run daily for automated updates.
