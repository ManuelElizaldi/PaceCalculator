### Example
# - Distance 21.01 km
# - Pace 7:49/km
# - Time 2h 44m

### Another example:
# - Distance 6.44 km
# - Pace 7:20/km
# - Time 47m 16s
import streamlit as st
from Functions import *

st.set_page_config(page_title="Pace Converter", page_icon="Resources\RunningIcon_Test.jpg", layout="wide")

# Header
st.subheader("Pace Calculator")

# Getting time variable
default_time = '2,44,0'
time = st.text_input("What was your time? Please enter format h,m,s:", default_time)
st.write('Example: *write what to do if mins = 0* ')

time_parts = time.split(',')

if len(time_parts) == 3:
    try:
        hours = float(time_parts[0])
        minutes = float(time_parts[1])
        seconds = float(time_parts[2])
    except ValueError:
        st.write("Invalid time format. Please enter hours, minutes, and seconds as numbers.")
else:
    st.write("Invalid time format. Please enter hours, minutes, and seconds separated by commas.")

# Distance
default_distance = '21.01'
distance = st.text_input("What distance did you run? Please enter format: 0,0", default_distance)
# Km or mi
measurement = st.selectbox('Are you measuring in kilometer or miles?', options=["Kilometers","Miles"])

# Calculating pace
# time, distance, measurement
pace = paceCalculator(time, distance, measurement)
st.write('Your running pace was:',pace,'minutes per ', measurement)

# # Header
st.subheader("Pace Converter")

# # Drop box -> selection if km or m
st.selectbox('What was your format, km or mi?', options=["Kilometers","Miles"])

# # Enter pace here
title = st.text_input("What was your pace?")

st.write('Your pace is:', title)