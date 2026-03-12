import pandas as pd

df = pd.read_csv("data/processed/deliveries_enriched.csv")

df.groupby("delivery_partner")["is_delayed"].mean() \
  .to_csv("analytics/partner_delay_summary.csv")

df.groupby("region")["delay_hours"].mean() \
  .to_csv("analytics/region_delay_summary.csv")

df.groupby("weather_condition")["delay_hours"].mean() \
  .to_csv("analytics/weather_delay_summary.csv")

print("Analytics summaries saved.")