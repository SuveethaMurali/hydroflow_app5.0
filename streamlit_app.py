import streamlit as st

st.title("🌧️ HydroFlow — Runoff Estimation App")
st.write("Choose your method to estimate surface runoff using SCN or Strangers Method.")

if st.button("Proceed to Method Selection ➡️"):
    st.switch_page("Method Selection")  # Must match sidebar page title exactly


