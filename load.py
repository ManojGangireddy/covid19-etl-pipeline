import psycopg2
import pandas as pd
from db_config import *

def load_data():
    # Read the cleaned data
    df = pd.read_csv("clean_covid_data.csv")

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS covid_stats (
            country TEXT,
            cases INTEGER,
            todayCases INTEGER,
            deaths INTEGER,
            todayDeaths INTEGER,
            recovered INTEGER,
            active INTEGER
        );
    """)

    # Insert each row into the table
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO covid_stats (country, cases, todayCases, deaths, todayDeaths, recovered, active)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, tuple(row))

    conn.commit()
    cur.close()
    conn.close()

    print("✅ Data loaded into PostgreSQL successfully.")

if __name__ == "__main__":
    load_data()
