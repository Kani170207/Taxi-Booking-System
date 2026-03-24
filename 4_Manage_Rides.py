import streamlit as st
import pandas as pd
from functions import view_data

st.set_page_config(page_title="Rides", layout="wide")

# Dark UI
st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 8px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)

st.title("📍 Ride History")

rides = view_data("rides")

if rides:
    # ✅ FIX: Remove column mismatch
    df = pd.DataFrame(rides)

    # ✅ OPTIONAL: Set proper column names (edit if needed)
    df.columns = [
        "Ride ID", "Driver ID", "Vehicle ID",
        "Pickup", "Drop", "Fare", "Status", "Created At"
    ]

    st.dataframe(df, use_container_width=True)
    st.caption(f"Total Rides: {len(df)}")

else:
    st.info("No rides available")