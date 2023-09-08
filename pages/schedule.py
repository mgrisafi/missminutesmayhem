import streamlit as st
import time
from datetime import datetime
from streamlit_sortables import sort_items
from streamlit_vis_timeline import st_timeline


attendees = ['Amr Abdel-Dayem', 'Lauralea Otis', 'Ahmad Mahdi', 'Eddie Drake', 'Jorge Alted', 'Matt Walters', 'Alice Taylor']

st.title('schedule')

tabs=['Priority', ' Date Range']

tab1, tab2 = st.tabs(tabs)

with tab1:

    sorted_items = sort_items(attendees)

with tab2:
    appointment = st.slider(
        "Select your date range:",
        min_value=datetime(2023, 9, 8, 9, 30),
        max_value=datetime(2023, 12, 31, 9, 30),
        value=(datetime(2023, 9, 8, 9, 30),datetime(2023, 12, 31, 9, 30)),
        format="dddd MMM DD YYYY")
    

with st.spinner('Calculating Possible Meeting Times'):
        time.sleep(5)
st.success('Calculated!')