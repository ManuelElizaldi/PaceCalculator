import streamlit as st

st.set_page_config(page_title="Pace Converter", page_icon="Resources\RunningIcon_Test.jpg", layout="wide")

# Header
st.subheader("Pace Converter")

# Drop box -> selection if km or m
st.selectbox('What was your format, km or mi?', options=["Kilometers","Miles"])

# Enter pace here
title = st.text_input("What was your pace?")

st.write('Your pace is:', title)