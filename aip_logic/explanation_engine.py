import pandas as pd

df = pd.read_csv("data/processed/deliveries_with_actions.csv")

def explain_risk(row):
    reasons = []

    if row["is_delayed"]:
        reasons.append("Delivery is delayed")

    if row["delay_severity"] == "high":
        reasons.append("High delay severity")

    if row["weather_condition"] in ["stormy", "rainy", "foggy"]:
        reasons.append("Bad weather conditions")

    if row["distance_km"] > 200:
        reasons.append("Long delivery distance")

    if row["risk_score"] > 10:
        reasons.append("Overall operational risk score is high")

    return ", ".join(reasons)

df["risk_explanation"] = df.apply(explain_risk, axis=1)

df.to_csv("data/processed/deliveries_with_explanations.csv", index=False)

print("Explanation engine executed successfully.")