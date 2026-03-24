import streamlit as st
from functions import view_data, add_driver, add_vehicle, add_ride

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Taxi Booking System", layout="wide")

# ------------------ LOGIN CHECK ------------------
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    st.warning("🔐 Please login first")
    st.switch_page("pages/0_Login.py")

# ------------------ SIDEBAR ------------------
st.sidebar.title("🚖 Taxi System")

# 🔐 Role display
if "role" in st.session_state:
    if st.session_state["role"] == "admin":
        st.sidebar.success("👑 Admin")
    else:
        st.sidebar.info("👤 User")

# 🚪 Logout button
if st.sidebar.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.switch_page("pages/0_Login.py")

# ------------------ MENU ------------------
menu = ["Add Driver", "Add Vehicle", "Book Ride", "View Data"]
choice = st.sidebar.selectbox("Menu", menu)

st.title("🚖 Taxi Booking System")

# ------------------ ADD DRIVER ------------------
if choice == "Add Driver":

    # 🔒 Only admin allowed
    if st.session_state.get("role") != "admin":
        st.error("⛔ Access denied")
        st.stop()

    st.subheader("👨‍✈️ Add Driver")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    license = st.text_input("License Number")

    if st.button("Add Driver"):
        add_driver(name, phone, license)
        st.success("✅ Driver Added Successfully")

# ------------------ ADD VEHICLE ------------------
elif choice == "Add Vehicle":

    # 🔒 Only admin allowed
    if st.session_state.get("role") != "admin":
        st.error("⛔ Access denied")
        st.stop()

    st.subheader("🚗 Add Vehicle")

    driver_id = st.number_input("Driver ID", min_value=1)
    model = st.text_input("Vehicle Model")
    plate = st.text_input("Plate Number")

    if st.button("Add Vehicle"):
        add_vehicle(driver_id, model, plate)
        st.success("✅ Vehicle Added")

# ------------------ BOOK RIDE ------------------
elif choice == "Book Ride":

    st.subheader("🚕 Book Ride")

    driver_id = st.number_input("Driver ID", min_value=1)
    vehicle_id = st.number_input("Vehicle ID", min_value=1)
    pickup = st.text_input("Pickup Location")
    dropoff = st.text_input("Drop Location")
    fare = st.number_input("Fare", min_value=0.0)
    status = st.selectbox("Status", ["Booked", "Completed"])

    if st.button("Book Ride"):
        add_ride(driver_id, vehicle_id, pickup, dropoff, fare, status)
        st.success("✅ Ride Booked")

# ------------------ VIEW DATA ------------------
elif choice == "View Data":

    # 🔒 Only admin allowed
    if st.session_state.get("role") != "admin":
        st.error("⛔ Access denied")
        st.stop()

    st.subheader("📊 View Data")

    table = st.selectbox("Select Table", ["drivers", "vehicles", "rides"])
    data = view_data(table)

    if data:
        import pandas as pd
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No data available")