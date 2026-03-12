import pandas as pd

# Load enriched delivery data
df = pd.read_csv("data/processed/deliveries_enriched.csv")

def recommend_action(row):
    actions = []

    # High risk deliveries
    if row["risk_score"] >= 10:
        actions.append("Escalate delivery to operations manager")

    # Severe delay
    if row["delay_severity"] == "high":
        actions.append("Notify delivery partner")

    # Weather impact
    if row["weather_condition"] in ["stormy", "rainy", "foggy"]:
        actions.append("Add buffer time for similar deliveries")

    # Long distance
    if row["distance_km"] > 200:
        actions.append("Consider alternate delivery partner")

    if not actions:
        actions.append("Monitor")

    return ", ".join(actions)

# Apply decision engine
df["recommended_action"] = df.apply(recommend_action, axis=1)

# Save results
df.to_csv("data/processed/deliveries_with_actions.csv", index=False)

print("Decision engine executed successfully.")