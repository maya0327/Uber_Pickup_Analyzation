# Uber_Pickup_Analyzation_And_Visualyzing
Uber Pickups Analysis – New York City
A data analysis project exploring Uber pickups in NYC using Python, Pandas, NumPy, and Jupyter Notebooks.
This repository includes code, environment setup instructions, and analysis guidelines for working with the fivethirtyeight/uber-pickups-in-new-york-city dataset.

Project Structure
uber-pickups-analysis/
│
├── data/                     # Dataset files (CSV files downloaded from Kaggle)
├── notebooks/
│     └── analysis.ipynb      # Jupyter Notebook with all analysis
├── src/
│     └── visualization.py
│
├── README.md
└── requirements.txt          # Python packages needed

Requirements
Before running the project, you must install:
1️. Python (3.10 or 3.12 recommended)
Download from: https://www.python.org/
Make sure to tick:
✔ "Add to PATH"

2️. VS Code
With extensions:
    • Python (Microsoft)
    • Jupyter Notebook
    
3. Install Required Libraries
Run these in VS Code terminal:
pip install pandas numpy matplotlib seaborn jupyter ipykernel kaggle
Then create a kernel for Jupyter:
python -m ipykernel install --user --name uber-env


Downloading the Dataset (Kaggle)
Step 1 — Setup Kaggle API
    1. Create a Kaggle account
    2. Go to: Account → API → Create New Token
    3. Download: kaggle.json
    
Step 2 — Move API Key
Place kaggle.json into:
C:\Users\<your-user>\.kaggle\
Then set permissions(optional):
chmod 600 ~/.kaggle/kaggle.json

Step 3 — Download the Dataset
Inside VS Code terminal:
kaggle datasets download -d fivethirtyeight/uber-pickups-in-new-york-city
Extract it:
unzip uber-pickups-in-new-york-city.zip -d data
Now all data is inside /data.

