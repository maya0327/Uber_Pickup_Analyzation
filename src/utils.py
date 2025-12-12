def print_summary(df):
    print("\n===== DATA SUMMARY =====")
    print(df.describe())
    print("\nMissing values:\n", df.isnull().sum())
    print("\nColumns:", df.columns.tolist())
