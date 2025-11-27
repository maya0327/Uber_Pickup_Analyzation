# src/preprocess.py
import os
import glob
import pandas as pd

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "uber_cleaned.csv")

# Common alternative names for datetime and lat/lon columns
DATETIME_KEYS = ["date/time", "date_time", "datetime", "date", "pickup_datetime", "date/time (utc)", "date/time"]
LAT_KEYS = ["lat", "latitude", "pickup_latitude"]
LON_KEYS = ["lon", "lng", "longitude", "pickup_longitude", "long"]

def find_column(cols, keys):
    cols_l = [c.lower().strip() for c in cols]
    for k in keys:
        if k in cols_l:
            return cols[cols_l.index(k)]
    # fuzzy: try if any col contains key substring
    for k in keys:
        for i,c in enumerate(cols_l):
            if k in c:
                return cols[i]
    return None

def load_all_csvs(data_dir):
    pattern = os.path.join(data_dir, "*.csv")
    files = sorted(glob.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No CSV files found in {data_dir}")
    dfs = []
    for f in files:
        try:
            df = pd.read_csv(f, low_memory=False)
            print(f"[LOAD] {os.path.basename(f)} -> {df.shape[0]} rows, {df.shape[1]} cols")
            df["__source_file"] = os.path.basename(f)
            dfs.append(df)
        except Exception as e:
            print(f"[ERROR] Failed to read {f}: {e}")
    combined = pd.concat(dfs, ignore_index=True, sort=False)
    return combined

def standardize(df):
    # locate datetime column
    dt_col = find_column(df.columns, DATETIME_KEYS)
    if dt_col is None:
        # try to infer: any column with 'time' or 'date' in name
        for c in df.columns:
            if "time" in c.lower() or "date" in c.lower():
                dt_col = c
                break
    if dt_col is None:
        raise RuntimeError("Could not find datetime column in dataset. Check your CSVs' headers.")

    print(f"[INFO] Using datetime column: '{dt_col}'")
    # parse datetimes robustly
    df[dt_col] = pd.to_datetime(df[dt_col], errors="coerce", infer_datetime_format=True)
    # rename to canonical name
    df = df.rename(columns={dt_col: "pickup_datetime"})

    # find lat/lon if present and rename
    lat_col = find_column(df.columns, LAT_KEYS)
    lon_col = find_column(df.columns, LON_KEYS)
    if lat_col and lon_col:
        df = df.rename(columns={lat_col: "lat", lon_col: "lon"})
        # drop obviously bad coords
        df = df[(df["lat"].notna()) & (df["lon"].notna())]
        # filter extreme values (optionally)
        df = df[(df["lat"].between(-90, 90)) & (df["lon"].between(-180, 180))]
    else:
        print("[WARN] lat/lon columns not found — mapping visualizations will be limited.")

    # drop rows with invalid datetimes
    before = len(df)
    df = df[df["pickup_datetime"].notna()]
    dropped = before - len(df)
    print(f"[INFO] Dropped {dropped} rows with invalid datetimes")

    # feature extraction
    df["hour"] = df["pickup_datetime"].dt.hour.astype("Int64")
    df["date"] = df["pickup_datetime"].dt.date
    df["day"] = df["pickup_datetime"].dt.day.astype("Int64")
    df["weekday"] = df["pickup_datetime"].dt.day_name()
    df["month"] = df["pickup_datetime"].dt.month.astype("Int64")
    df["year"] = df["pickup_datetime"].dt.year.astype("Int64")

    # optional: simple dedupe by datetime + lat + lon
    if {"lat","lon"}.issubset(df.columns):
        df = df.drop_duplicates(subset=["pickup_datetime","lat","lon"])
    else:
        df = df.drop_duplicates(subset=["pickup_datetime","__source_file"])

    return df

def main():
    print("[START] Preprocessing")
    df = load_all_csvs(DATA_DIR)
    df = standardize(df)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"[DONE] Cleaned dataset saved at: {OUTPUT_FILE}")
    print(df.info())
    print(df.head())

if __name__ == "__main__":
    main()
