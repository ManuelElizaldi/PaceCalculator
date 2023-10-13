### Example
# - Distance 21.01 km
# - Pace 7:49/km
# - Time 2h 44m

### Another example:
# - Distance 6.44 km
# - Pace 7:20/km
# - Time 47m 16s
import streamlit as st
import pandas as pd
from Functions import *

st.set_page_config(page_title="Pace Converter", page_icon="RunningIcon_Test.jpg", layout="centered", menu_items=None)
    
# Pace conversion section
st.subheader("Pace Converter")

# Drop box -> selection if km or m
measurement_conver = st.selectbox('Are you measuring in Miles or Kilometers?', options=["Kilometers","Miles"])

# Enter pace here
default_pace = '7.48'
pace_conver = st.text_input("What was your pace?", default_pace)

# Applying function for conversion
try:
    pace_conversion = paceConverter(measurement_conver, pace_conver)
except:
    st.write('Please enter your pace in the correct format: 0.0')

# Pace calculator secion
st.subheader("Pace Calculator")

# Getting time variable
default_time = '2:44:0'
time = st.text_input("What was your time? Please enter hours, minutes, and seconds separated by ':'. h:m:s", default_time)

# Distance
default_distance = '21.01'
distance = st.text_input("What distance did you run? Please enter value separated by commas: 0,0", default_distance)
# Km or mi
measurement = st.selectbox('Are you measuring in kilometer or miles?', options=["Kilometers","Miles"])
# Calculating pace with function from Functions.py file
# time, distance, measurement
try:
    pace = paceCalculator(time, distance, measurement)
    
except ValueError as e:
    pace = str(e)
    st.write('Invalid time format. Please enter hours, minutes, and seconds separated by ":"')
    
# Km to mile converter     
st.subheader("Unit Conversion")

# Drop box -> selection if km or m 
conversion = st.selectbox('From', options=["Kilometers","Miles"])
distance_to_convert = st.text_input("Enter your distance", '10')

result = UnitConverter(conversion, distance_to_convert)

# try:
#     distance_conversion = UnitConverter(conversion, distance_to_convert)
    
# except ValueError as e:
#     distance_conversion = str(e)
#     st.write('Invalid unit format. Please enter a number.')

st.write()

# Common pace and times table, getting data from excel file
df = pd.DataFrame(df)
st.dataframe(df.set_index(df.columns[0]))

