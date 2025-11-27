# src/visualize.py
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
INPUT_FILE = os.path.join(OUTPUT_DIR, "uber_cleaned.csv")

def load_data(path=INPUT_FILE):
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found. Run preprocess first.")
    df = pd.read_csv(path, parse_dates=["pickup_datetime"], low_memory=False)
    return df

def plot_pickups_by_hour(df, savepath):
    counts = df.groupby("hour").size().reindex(range(0,24), fill_value=0)
    plt.figure(figsize=(10,5))
    sns.barplot(x=counts.index, y=counts.values)
    plt.title("Pickups by Hour of Day")
    plt.xlabel("Hour (0-23)")
    plt.ylabel("Number of Pickups")
    plt.tight_layout()
    plt.savefig(savepath)
    plt.close()
    print(f"[SAVED] {savepath}")

def plot_pickups_by_weekday(df, savepath):
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    counts = df.groupby("weekday").size().reindex(order, fill_value=0)
    plt.figure(figsize=(9,5))
    sns.barplot(x=counts.index, y=counts.values)
    plt.xticks(rotation=15)
    plt.title("Pickups by Weekday")
    plt.ylabel("Number of Pickups")
    plt.tight_layout()
    plt.savefig(savepath)
    plt.close()
    print(f"[SAVED] {savepath}")

def plot_heatmap_hour_weekday(df, savepath):
    pivot = df.groupby(["weekday","hour"]).size().unstack(fill_value=0)
    # reindex rows in weekday order
    order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    pivot = pivot.reindex(order)
    plt.figure(figsize=(12,6))
    sns.heatmap(pivot, cmap="viridis")
    plt.title("Heatmap: Pickups (weekday vs hour)")
    plt.ylabel("Weekday")
    plt.xlabel("Hour of Day")
    plt.tight_layout()
    plt.savefig(savepath)
    plt.close()
    print(f"[SAVED] {savepath}")

def scatter_latlon(df, savepath, n_sample=50000):
    if not {"lat","lon"}.issubset(df.columns):
        print("[WARN] lat/lon not available — skipping scatter map.")
        return
    sample = df.sample(min(len(df), n_sample), random_state=1)
    plt.figure(figsize=(6,6))
    plt.scatter(sample["lon"], sample["lat"], s=1, alpha=0.4)
    plt.title("Pickup locations (sample)")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.tight_layout()
    plt.savefig(savepath, dpi=150)
    plt.close()
    print(f"[SAVED] {savepath}")

def folium_map(df, savepath, n_sample=1000):
    if not {"lat","lon"}.issubset(df.columns):
        print("[WARN] lat/lon not available — skipping folium map.")
        return
    sample = df.sample(min(len(df), n_sample), random_state=2)
    center = [sample["lat"].mean(), sample["lon"].mean()]
    m = folium.Map(location=center, zoom_start=12)
    for _, r in sample.iterrows():
        folium.CircleMarker(location=[r["lat"], r["lon"]],
                            radius=2, opacity=0.6, fill=True).add_to(m)
    m.save(savepath)
    print(f"[SAVED] {savepath}")

def main():
    print("[START] Visualizations")
    df = load_data()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    plot_pickups_by_hour(df, os.path.join(OUTPUT_DIR, "pickups_by_hour.png"))
    plot_pickups_by_weekday(df, os.path.join(OUTPUT_DIR, "pickups_by_weekday.png"))
    plot_heatmap_hour_weekday(df, os.path.join(OUTPUT_DIR, "heatmap_weekday_hour.png"))
    scatter_latlon(df, os.path.join(OUTPUT_DIR, "pickup_locations_sample.png"))
    folium_map(df, os.path.join(OUTPUT_DIR, "uber_map.html"))

    print("[DONE] All visualizations saved to data/")

if __name__ == "__main__":
    main()
