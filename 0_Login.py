import streamlit as st
from functions import login_user

st.set_page_config(page_title="Login", layout="centered")

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    result = login_user(username, password)

    if result:
        st.session_state["logged_in"] = True
        st.session_state["role"] = result[0]
        st.success("Login successful")
        st.switch_page("app.py")
    else:
        st.error("Invalid credentials")