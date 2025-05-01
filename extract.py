import requests
import pandas as pd

def extract_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data)
        df.to_csv("raw_covid_data.csv", index=False)
        print("✅ Data extracted and saved to raw_covid_data.csv")
    else:
        print(f"❌ Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    extract_data()
