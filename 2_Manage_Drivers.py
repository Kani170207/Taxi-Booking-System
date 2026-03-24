import streamlit as st
import pandas as pd
from functions import add_driver, view_data, delete_driver

# Page config (ONLY ONCE at top)
st.set_page_config(page_title="Taxi Booking System", layout="wide")

# ✅ Premium Dark UI (keep only once)
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
    width: 100%;
}

.stTextInput>div>div>input {
    border-radius: 8px;
}

/* Table styling */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.title("👨‍✈️ Drivers Management")

col1, col2 = st.columns([1, 2])

# ---------------- LEFT: ADD DRIVER ----------------
with col1:
    st.subheader("➕ Add Driver")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    license = st.text_input("License")

    if st.button("Add Driver"):
        if name and phone and license:
            add_driver(name, phone, license)
            st.success("Driver Added Successfully 🚀")
        else:
            st.warning("Please fill all fields")

# ---------------- RIGHT: VIEW + DELETE ----------------
with col2:
    st.subheader("📋 Driver List")

    data = view_data("drivers")

    if data:
        df = pd.DataFrame(data, columns=[
            "Driver ID", "Name", "Phone", "License"
        ])

        # ✅ Premium table
        st.dataframe(df, use_container_width=True)

        # ✅ Extra info
        st.caption(f"Total Drivers: {len(df)}")

        st.divider()

        # DELETE SECTION
        st.subheader("🗑 Delete Driver")

        delete_id = st.number_input("Enter Driver ID", min_value=1)

        if st.button("Delete Driver"):
            delete_driver(delete_id)
            st.success("Driver Deleted ✅")
            st.rerun()

    else:
        st.info("No drivers available")