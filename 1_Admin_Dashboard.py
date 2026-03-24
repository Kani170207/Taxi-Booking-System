import streamlit as st
from functions import view_data

st.set_page_config(page_title="Dashboard", layout="wide")

# Dark UI
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Admin Dashboard")

drivers = view_data("drivers")
vehicles = view_data("vehicles")
rides = view_data("rides")

col1, col2, col3 = st.columns(3)

col1.metric("👨‍✈️ Drivers", len(drivers))
col2.metric("🚗 Vehicles", len(vehicles))
col3.metric("📍 Rides", len(rides))

st.divider()

st.subheader("📍 System Overview")

st.info("Use the sidebar to manage drivers, vehicles and rides.")