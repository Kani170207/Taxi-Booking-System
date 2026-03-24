import streamlit as st

st.title("🚕 User Login")

user = st.text_input("Username")
pwd = st.text_input("Password", type="password")

if st.button("Login"):
    if user == "user" and pwd == "user123":
        st.session_state["user"] = True
        st.switch_page("pages/book_ride.py")
    else:
        st.error("Invalid credentials")