import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_hourly_trips(df):
    plt.figure(figsize=(10,5))
    sns.countplot(x='hour', data=df)
    plt.title("Uber Trips by Hour of Day")
    plt.savefig("../plots/hourly_trips.png")
    plt.show()

def plot_weekday_trips(df):
    plt.figure(figsize=(10,5))
    sns.countplot(x='weekday', data=df)
    plt.title("Uber Trips by Weekday")
    plt.savefig("../plots/weekday_trips.png")
    plt.show()

def plot_monthly_trips(df):
    plt.figure(figsize=(10,5))
    sns.countplot(x='month', data=df)
    plt.title("Uber Trips by Month")
    plt.savefig("../plots/monthly_trips.png")
    plt.show()

def plot_lat_long(df):
    plt.figure(figsize=(8,6))
    sns.scatterplot(x='Lon', y='Lat', data=df, s=10)
    plt.title("Uber Pick-ups Location Distribution")
    plt.savefig("../plots/location.png")
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("../data/uber_cleaned.csv")
    plot_hourly_trips(df)
    plot_weekday_trips(df)
    plot_monthly_trips(df)
    plot_lat_long(df)
