import streamlit as st

st.title("Method Selection")

method = st.radio("Select a method:", ["SCN Method", "Strangers Method"])

if st.button("Continue ➡️"):
    if method == "SCN Method":
        st.session_state.method = "scn"
        st.switch_page("2_SCN_Method.py")
    else:
        st.session_state.method = "strangers"
        st.switch_page("3_Strangers_Method.py")
