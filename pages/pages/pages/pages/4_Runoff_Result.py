import streamlit as st
import pandas as pd

st.title("💧 Runoff Result")

if "result" not in st.session_state:
    st.warning("No calculation found. Please go back to method page.")
    st.stop()

runoff = st.session_state.result
st.success(f"Estimated Runoff = {runoff:.2f} mm")

# Example hydrograph
x = [0, 1, 2, 3, 4, 5]
y = [0, runoff/2, runoff, runoff/1.5, runoff/3, 0]
df = pd.DataFrame({"Time (hr)": x, "Runoff (mm)": y})

st.line_chart(df)
st.dataframe(df)
