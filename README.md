Uber Pickups Analysis

## Overview
This project analyzes Uber pickup data in New York City and visualizes patterns in:
- Hourly activity
- Daily/weekly trends
- Monthly trends
- Latitude/Longitude pickup distribution

## Project Structure
- `src/preprocess.py` → Cleans the dataset
- `src/visualize.py` → Generates visualizations
- `notebook/analysis.ipynb` → Full exploratory analysis
- `data/` → Raw and cleaned datasets

## How to Run
```bash
pip install -r requirements.txt
python src/preprocess.py
python src/visualize.py

Before running the project, you must install:

1️⃣ Python (3.10 or 3.12 recommended)

Download from: https://www.python.org/

Make sure to tick:
✔ "Add to PATH"

2️⃣ VS Code

With extensions:

Python (Microsoft)

Jupyter Notebook

3️⃣ Install Required Libraries

Run these in VS Code terminal:

pip install pandas numpy matplotlib seaborn jupyter ipykernel kaggle


Then create a kernel for Jupyter:

python -m ipykernel install --user --name uber-env

📥 Downloading the Dataset (Kaggle)
Step 1 — Setup Kaggle API

Create a Kaggle account

Go to: Account → API → Create New Token

Download: kaggle.json

Step 2 — Move API Key

Place kaggle.json into:

C:\Users\<your-user>\.kaggle\


Then set permissions:

chmod 600 ~/.kaggle/kaggle.json

Step 3 — Download the Dataset

Inside VS Code terminal:

kaggle datasets download -d fivethirtyeight/uber-pickups-in-new-york-city


Extract it:

unzip uber-pickups-in-new-york-city.zip -d data


Now all data is inside /data.

▶️ Running the Project
1. Open VS Code

Open your project folder.

2. Create or Open the Notebook

Go to:

notebooks/analysis.ipynb


Select the kernel:

uber-env

3. Run a Test Cell
import pandas as pd

df = pd.read_csv("../data/uber-raw-data-apr14.csv")
df.head()


If you see a table → everything works!

🧪 Analysis Ideas

You can explore:

✔ Total pickups per month
✔ Peak pickup hours
✔ Which days are busiest
✔ Which locations have the highest demand
✔ Heatmaps of pickup times
✔ Pickup counts by borough

Example snippet:

df['Date/Time'] = pd.to_datetime(df['Date/Time'])
df['hour'] = df['Date/Time'].dt.hour

df.groupby('hour')['Base'].count().plot(kind='bar')

🌐 Adding Collaborators

Go to your GitHub repo:

Click Settings

Click Collaborators

Click Add People

Enter their GitHub usernames

Send email confirmation link (they must accept)

📤 Pushing Code to GitHub
First time:
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main

Updates:
git add .
git commit -m "Updated analysis"
git push

❓ Troubleshooting
FileNotFoundError

Means your code can’t locate the dataset.

Fix by using the correct relative path:

df = pd.read_csv("../data/yourfile.csv")


or absolute path.
