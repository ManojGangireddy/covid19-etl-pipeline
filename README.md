# COVID-19 ETL Pipeline

This project builds a simple end-to-end ETL pipeline in Python that extracts COVID-19 data from a public API, transforms it using pandas, loads it into a PostgreSQL database, and visualizes the top 5 most affected countries.

## 🛠 Tech Stack
- Python 3.9
- PostgreSQL (via Homebrew on macOS)
- Pandas, Requests, psycopg2, Matplotlib
- VS Code

## 🔄 Workflow
1. **Extract**: Fetch data from `disease.sh` API (`extract.py`)
2. **Transform**: Clean & sort with pandas (`transform.py`)
3. **Load**: Insert into PostgreSQL (`load.py`)
4. **Visualize**: Show top 5 countries (`visualize.py`)

## 📊 Output
The script generates a `top5_covid_cases.png` chart showing the most affected countries by total cases.

## 🗃 Database Schema
```sql
CREATE TABLE covid_stats (
    country TEXT,
    cases INTEGER,
    todayCases INTEGER,
    deaths INTEGER,
    todayDeaths INTEGER,
    recovered INTEGER,
    active INTEGER
);
