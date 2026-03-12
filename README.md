# Supply Chain Intelligence System

This project implements an operational analytics platform for logistics delivery data.

The system transforms raw delivery data into operational intelligence through a multi-layer architecture.

## System Architecture

Raw Data → Data Pipeline → Analytics → Decision Engine → Dashboard

## Components

### Data Pipeline
Transforms raw delivery records into enriched operational data including:
- delay hours
- delay severity
- operational risk score
- performance classification

### Analytics Layer
Generates operational insights including:
- delivery partner delay rates
- regional delay trends
- weather impact on deliveries

### Decision Engine
Applies operational logic to identify high-risk deliveries and generate recommended actions.

### Explanation Engine
Provides interpretable explanations describing why deliveries are considered high risk.

### Operational Dashboard
A Streamlit-based command center to monitor delivery performance and operational risk.

## Technologies Used

- Python
- Pandas
- Streamlit
- NumPy

## Use Case

The system demonstrates how logistics teams could monitor delivery performance and respond proactively to operational risks.

## Running the Dashboard

Install dependencies:

pip install -r requirements.txt

Run the dashboard:

streamlit run app/dashboard.py