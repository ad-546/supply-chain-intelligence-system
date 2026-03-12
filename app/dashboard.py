import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/deliveries_with_explanations.csv")

st.title("Supply Chain Intelligence Command Center")

# ---- KPI Metrics ----
st.subheader("Operational Overview")

total_deliveries = len(df)
delayed_deliveries = df["is_delayed"].sum()
avg_delay = df["delay_hours"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Deliveries", total_deliveries)
col2.metric("Delayed Deliveries", delayed_deliveries)
col3.metric("Average Delay (hours)", round(avg_delay,2))

st.subheader("System Performance Metrics")

avg_cost = df["delivery_cost"].mean()
avg_rating = df["delivery_rating"].mean()
avg_distance = df["distance_km"].mean()

col4, col5, col6 = st.columns(3)

col4.metric("Average Delivery Cost", round(avg_cost, 2))
col5.metric("Average Delivery Rating", round(avg_rating, 2))
col6.metric("Average Distance (km)", round(avg_distance, 2))

# ---- Filters ----
st.sidebar.header("Filters")

region_filter = st.sidebar.selectbox(
    "Select Region",
    ["All"] + list(df["region"].unique())
)

if region_filter != "All":
    df = df[df["region"] == region_filter]

# ---- Partner Delay Chart ----
st.subheader("Delivery Partner Delay Rate")
partner_delay = df.groupby("delivery_partner")["is_delayed"].mean()
st.bar_chart(partner_delay)

# ---- Weather Impact ----
st.subheader("Weather Impact on Delay")
weather_delay = df.groupby("weather_condition")["delay_hours"].mean()
st.bar_chart(weather_delay)

# ---- Risk Deliveries ----
st.subheader("High Risk Deliveries")

top_risk = df.sort_values("risk_score", ascending=False).head(20)
st.dataframe(top_risk)

# ---- Recommended Actions ----
st.subheader("Recommended Operational Actions")

actions = df[["delivery_id","delivery_partner","region","recommended_action"]]
st.dataframe(actions.head(20))
st.subheader("AI Risk Explanations")

explain_table = df[
    ["delivery_id", "delivery_partner", "risk_score", "risk_explanation"]
].sort_values("risk_score", ascending=False).head(20)

st.dataframe(explain_table)

st.subheader("Operational Performance Distribution")
band_counts = df["performance_band"].value_counts()
st.bar_chart(band_counts)