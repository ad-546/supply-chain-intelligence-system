import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/deliveries.csv")

# Normalize delayed column (handle Yes/No, 1/0, True/False)
df["delayed_flag"] = df["delayed"].astype(str).str.lower().isin(
    ["1", "true", "yes", "y"]
)

# Create proxy delay_hours (business assumption)
df["delay_hours"] = np.where(
    df["delayed_flag"],
    df["distance_km"] / 40,   # proxy: avg 40 km/hr delay impact
    0
)

df["is_delayed"] = df["delayed_flag"]

def delay_severity(hours):
    if hours == 0:
        return "on_time"
    elif hours <= 2:
        return "low"
    elif hours <= 5:
        return "medium"
    else:
        return "high"

df["delay_severity"] = df["delay_hours"].apply(delay_severity)

# Risk score (interpretable)
df["risk_score"] = (
    df["is_delayed"].astype(int) * 3 +
    (df["distance_km"] / 100) +
    (df["package_weight_kg"] / 10)
)

def performance_band(row):
    if row["is_delayed"] and row["delivery_rating"] < 3:
        return "Critical"
    elif row["is_delayed"]:
        return "At Risk"
    elif row["delivery_rating"] >= 4:
        return "High Performing"
    else:
        return "Stable"

df["performance_band"] = df.apply(performance_band, axis=1)


df.to_csv("data/processed/deliveries_enriched.csv", index=False)

print("Pipeline executed successfully with proxy delay logic.")

