import pandas as pd
import numpy as np

# 1. Load data and fix time strings
crimes = pd.read_csv("crimes.csv", dtype={"TIME OCC": str})
crimes["HOUR ONLY"] = crimes["TIME OCC"].str.zfill(4).str[:2].astype(int)

# 2. Peak Crime Hour
peak_crime_hour = int(crimes["HOUR ONLY"].value_counts().idxmax())

# 3. Night Crimes Location (10pm to 3:59am)
night_crimes = crimes[(crimes["HOUR ONLY"] >= 22) | (crimes["HOUR ONLY"] <= 3)] 
peak_night_crime_location = str(night_crimes["AREA NAME"].value_counts().idxmax())

# 4. Victim Age Demographics
age_bins = [0, 17, 25, 34, 44, 54, 64, np.inf]
age_labels = ["0-17", "18-25", "26-34", "35-44", "45-54", "55-64", "65+"]
crimes["AGE_GROUP"] = pd.cut(crimes["Vict Age"], bins=age_bins, labels=age_labels, include_lowest=True)
victim_ages = crimes["AGE_GROUP"].value_counts().sort_index()

print("Analysis Complete!")
