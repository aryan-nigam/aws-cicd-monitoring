
import os
import pandas as pd
import streamlit as st

CSV_FILE = "monitor_history.csv"

st.set_page_config(
    page_title="SRE Monitoring Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Application Health Monitoring Dashboard")
st.caption("AWS CI/CD & Infrastructure Monitoring Pipeline")

if st.button("Refresh dashboard"):
    st.rerun()

if not os.path.exists(CSV_FILE):
    st.warning("No monitoring history found. Run monitor.py first.")
    st.stop()

df = pd.read_csv(CSV_FILE)

if df.empty:
    st.warning("The monitoring history is empty.")
    st.stop()

df["response_time_ms"] = pd.to_numeric(
    df["response_time_ms"], errors="coerce"
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"], errors="coerce"
)

total_checks = len(df)
successful_checks = (df["status"] == "HEALTHY").sum()
failed_checks = total_checks - successful_checks

availability = successful_checks / total_checks * 100

average_response_time = df["response_time_ms"].mean()

st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Health Checks", total_checks)
col2.metric("Availability", f"{availability:.2f}%")
col3.metric("Failed Checks", int(failed_checks))

if pd.notna(average_response_time):
    col4.metric(
        "Average Response Time",
        f"{average_response_time:.2f} ms"
    )
else:
    col4.metric("Average Response Time", "N/A")

st.divider()

st.subheader("Response Time History")

chart_data = df.dropna(
    subset=["timestamp", "response_time_ms"]
).set_index("timestamp")

if not chart_data.empty:
    st.line_chart(chart_data["response_time_ms"])
else:
    st.info("No response-time data is available yet.")

st.subheader("Health Status Distribution")

status_counts = df["status"].value_counts()
st.bar_chart(status_counts)

st.subheader("Recent Health Checks")

st.dataframe(
    df.tail(20).iloc[::-1],
    use_container_width=True,
    hide_index=True
)
