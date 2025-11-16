import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    # try common datetime column names
    if 'DateTime' in df.columns:
        dtcol = 'DateTime'
    elif 'date/time' in df.columns:
        dtcol = 'date/time'
    else:
        # fallback: first column that looks like datetime
        dtcol = df.columns[0]

    df[dtcol] = pd.to_datetime(df[dtcol], errors='coerce')
    df = df.dropna(subset=[dtcol])
    df = df.rename(columns={dtcol: 'DateTime'})
    df['hour'] = df['DateTime'].dt.hour
    df['day'] = df['DateTime'].dt.day
    df['weekday'] = df['DateTime'].dt.weekday
    return df
