import streamlit as st
import pandas as pd
import numpy as np

#Custom Functions
#----------------------

@st.cache
def load_data(location):
    data = pd.read_csv(location)
    return data

#Page Design
#-----------------------
#Title
st.title('Toronto Daily Shelter Occupancy Rate')

st.write('Let us take a quick look into the Daily Shelter Occupancy Rate in Toronto')

data_path = 'data/to_shelter_occupancy_2020.csv'
df = load_data(data_path)

#Show Data
st.dataframe(df)

cols = ['OCCUPANCY_DATE','SECTOR','CAPACITY', 'OCCUPANCY']
st_ms = st.multiselect("Columns", df.columns.tolist(),default = cols)








if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
