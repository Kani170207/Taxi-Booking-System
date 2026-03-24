import streamlit as st
st.set_page_config(page_title="Taxi Booking System", layout="wide")

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
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
</style>
""", unsafe_allow_html=True)
import streamlit as st
import pandas as pd
from functions import add_vehicle, view_data

st.title("🚗 Vehicles Management")

drivers = view_data("drivers")

driver_dict = {f"{d[1]} (ID {d[0]})": d[0] for d in drivers}

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("➕ Add Vehicle")

    if drivers:
        driver = st.selectbox("Driver", list(driver_dict.keys()))
        model = st.text_input("Model")
        plate = st.text_input("Plate")

        if st.button("Add Vehicle"):
            add_vehicle(driver_dict[driver], model, plate)
            st.success("Added")
    else:
        st.warning("Add drivers first")

with col2:
    st.subheader("📋 Vehicles List")

    vehicles = view_data("vehicles")

    if vehicles:
        df = pd.DataFrame(vehicles, columns=[
            "ID", "Driver ID", "Model", "Plate"
        ])
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No vehicles yet")
        st.markdown("""
<style>
body {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 3em;
}
</style>
""", unsafe_allow_html=True)