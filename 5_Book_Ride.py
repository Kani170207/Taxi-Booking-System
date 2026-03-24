import streamlit as st
from functions import add_ride, view_data

st.set_page_config(page_title="Book Ride", layout="wide")

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

st.title("🚕 Book a Ride")

drivers = view_data("drivers")
vehicles = view_data("vehicles")

driver_dict = {f"{d[1]} (ID {d[0]})": d[0] for d in drivers}
vehicle_dict = {f"{v[2]} (ID {v[0]})": v[0] for v in vehicles}

col1, col2 = st.columns(2)

with col1:
    driver = st.selectbox("Select Driver", list(driver_dict.keys()))
    pickup = st.text_input("Pickup Location")

with col2:
    vehicle = st.selectbox("Select Vehicle", list(vehicle_dict.keys()))
    drop = st.text_input("Drop Location")

fare = st.number_input("Fare", min_value=0.0)

if st.button("🚀 Confirm Booking"):
    if pickup and drop:
        add_ride(
            driver_dict[driver],
            vehicle_dict[vehicle],
            pickup,
            drop,
            fare,
            "Booked"
        )
        st.success("Ride Booked Successfully 🚀")
    else:
        st.warning("Please fill all fields")