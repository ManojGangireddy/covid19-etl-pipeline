import pandas as pd

def transform_data():
    # Load the raw data
    df = pd.read_csv("raw_covid_data.csv")

    # Select important columns
    selected_cols = ['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active']
    df = df[selected_cols]

    # Sort by total cases (descending)
    df = df.sort_values(by='cases', ascending=False)

    # Save the cleaned data
    df.to_csv("clean_covid_data.csv", index=False)
    print("✅ Data transformed and saved to clean_covid_data.csv")

if __name__ == "__main__":
    transform_data()
