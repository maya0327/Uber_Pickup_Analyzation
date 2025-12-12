import pandas as pd

def load_data(path):
    """Load raw Uber CSV file."""
    return pd.read_csv(path)

def clean_data(df):
    """Clean Uber dataset (datetime, missing values, duplicates)."""
    df = df.copy()

    # Convert columns
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], errors='coerce')

    # Remove null values
    df = df.dropna()

    # Remove duplicates
    df = df.drop_duplicates()

    # Extract useful features
    df['hour'] = df['Date/Time'].dt.hour
    df['day'] = df['Date/Time'].dt.day
    df['weekday'] = df['Date/Time'].dt.weekday
    df['month'] = df['Date/Time'].dt.month

    return df

def save_cleaned_data(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset saved to {output_path}")


if __name__ == "__main__":
    raw_path = "../data/uber-raw-data-apr14.csv"
    cleaned_path = "../data/uber_cleaned.csv"

    df = load_data(raw_path)
    cleaned_df = clean_data(df)
    save_cleaned_data(cleaned_df, cleaned_path)
