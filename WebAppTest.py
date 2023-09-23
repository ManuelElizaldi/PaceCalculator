import streamlit as st

st.set_page_config(page_title="Pace Converter", page_icon="Resources\RunningIcon_Test.jpg", layout="wide")

# Header for
st.subheader("Pace Converter")
st.selectbox('What was your format, km or mi?', options=["Kilometers","Miles"])