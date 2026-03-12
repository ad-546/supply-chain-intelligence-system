import pandas as pd

df = pd.read_csv("data/processed/deliveries_enriched.csv")

# Partner delay rate
partner_delay = df.groupby("delivery_partner")["is_delayed"].mean()
partner_delay.to_csv("analytics/partner_delay_rate.csv")

# Region average delay
region_delay = df.groupby("region")["delay_hours"].mean()
region_delay.to_csv("analytics/region_avg_delay_hours.csv")

# Weather impact
weather_delay = df.groupby("weather_condition")["delay_hours"].mean()
weather_delay.to_csv("analytics/weather_delay_hours.csv")

# Top risk deliveries
top_risk = df.sort_values("risk_score", ascending=False).head(20)
top_risk.to_csv("analytics/top_20_high_risk_deliveries.csv", index=False)

print("Week 1 analytics outputs saved.")