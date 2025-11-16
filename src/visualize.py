import matplotlib.pyplot as plt
import seaborn as sns

def plot_hourly(df, show=True, savepath=None):
    plt.figure(figsize=(10,4))
    sns.countplot(x='hour', data=df)
    plt.title("Pickups by hour")
    plt.xlabel("Hour of day")
    plt.ylabel("Count")
    if savepath:
        plt.savefig(savepath, bbox_inches='tight')
    if show:
        plt.show()
    plt.close()
