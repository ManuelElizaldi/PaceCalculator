import streamlit as st
from paceConverter import *

st.set_page_config(page_title="Pace Converter", page_icon="Resources\RunningIcon_Test.jpg", layout="wide")

# Header
st.subheader("Pace Calculator")

distance = st.text_input("What distance did you run? Please enter format: 0,0")

time = st.text_input("What was your time? Please enter format h,m,s:")

# Drop box -> selection if km or m
measurement = st.selectbox('Are you measuring in kilometer or miles?', options=["Kilometers","Miles"])


pace = paceCalculator(time, distance, measurement)

st.write('Your pace is:', pace)

# Header
st.subheader("Pace Converter")

# Drop box -> selection if km or m
st.selectbox('What was your format, km or mi?', options=["Kilometers","Miles"])

# Enter pace here
title = st.text_input("What was your pace?")

st.write('Your pace is:', title)