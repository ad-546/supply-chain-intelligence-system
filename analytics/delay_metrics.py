import pandas as pd

df = pd.read_csv("data/processed/deliveries_enriched.csv")

print("\n===== BASIC DATA CHECK =====")
print(df.head())
print(df.info())

print("\n===== DELAY RATE BY DELIVERY PARTNER =====")
partner_delay = (
    df.groupby("delivery_partner")["is_delayed"]
    .mean()
    .sort_values(ascending=False)
)
print(partner_delay)

print("\n===== AVERAGE DELAY (HOURS) BY REGION =====")
region_delay = (
    df.groupby("region")["delay_hours"]
    .mean()
    .sort_values(ascending=False)
)
print(region_delay)

print("\n===== DELAY BY WEATHER CONDITION =====")
weather_delay = (
    df.groupby("weather_condition")["delay_hours"]
    .mean()
    .sort_values(ascending=False)
)
print(weather_delay)

print("\n===== TOP 10 HIGHEST RISK DELIVERIES =====")
top_risk = df.sort_values("risk_score", ascending=False).head(10)
print(top_risk[
    ["delivery_id", "delivery_partner", "region",
     "delay_hours", "risk_score"]
])