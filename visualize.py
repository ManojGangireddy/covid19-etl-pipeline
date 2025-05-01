import pandas as pd
import matplotlib.pyplot as plt

def visualize_top5():
    # Load the cleaned data
    df = pd.read_csv("clean_covid_data.csv")

    # Take top 5 countries by case count
    top5 = df.head(5)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.bar(top5['country'], top5['cases'], color='tomato')
    plt.title('Top 5 Countries by Total COVID-19 Cases')
    plt.xlabel('Country')
    plt.ylabel('Total Cases')
    plt.tight_layout()
    plt.savefig("top5_covid_cases.png")
    plt.show()
    print("✅ Visualization created and saved as top5_covid_cases.png")

if __name__ == "__main__":
    visualize_top5()
