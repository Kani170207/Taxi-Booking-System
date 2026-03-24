import streamlit as st

st.set_page_config(page_title="Admin Login", layout="centered")

st.title("👨‍💼 Admin Login")

user = st.text_input("Username")
pwd = st.text_input("Password", type="password")

if st.button("Login"):
    if user == "admin" and pwd == "admin123":
        st.session_state["admin"] = True
        st.switch_page("pages/admin_dashboard.py")
    else:
        st.error("Invalid credentials")