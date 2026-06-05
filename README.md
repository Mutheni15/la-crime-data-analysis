# Los Angeles Crime Data Analysis (LAPD)

## 📌 Project Overview
This project analyzes crime incidents reported in Los Angeles to uncover critical patterns regarding **when** crimes occur, **where** they happen most frequently at night, and **who** the primary victims are. 

By leveraging Python and Pandas, this analysis transforms raw operational logs into actionable insights that could help city planners and law enforcement optimize resource allocation.

---

## 🛠️ Tech Stack & Key Concepts
* **Language:** Python
* **Libraries:** Pandas, NumPy
* **Key Techniques:** Vectorized string manipulation, data type enforcement during ingestion, data binning (`pd.cut`), and logical data masking.

---

## 🔍 Key Findings & Data Engineering Challenges

### 1. Peak Crime Hour
* **The Challenge:** The raw `TIME OCC` column stores military time as integers, which strips leading zeros (e.g., `615` instead of `0615`). Slicing this directly would incorrectly flag the hour as `61`. 
* **The Solution:** Enforced string types on import, applied `.str.zfill(4)` to standardize lengths, and sliced the first two characters to cleanly extract the peak hour.

### 2. High-Risk Nighttime Locations (10:00 PM - 3:59 AM)
* **The Challenge:** Filtering hours that cross over the midnight threshold requires complex conditional logic because an hour cannot simultaneously be greater than 22 and less than 3.
* **The Solution:** Implemented a logical OR mask (`|`) to isolate night-shift data, identifying **Central** as the highest frequency area for night crimes.

### 3. Victim Age Demographics
* **The Challenge:** Raw age numbers are too granular to show meaningful trends, and data entry anomalies (like `0` for unknown ages) skew standard averages.
* **The Solution:** Utilized `pd.cut()` with a numeric `np.inf` upper bound and careful boundary inclusion parameters (`include_lowest=True`) to segment victims into clean, standard chronological age brackets.
