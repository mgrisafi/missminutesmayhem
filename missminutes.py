import streamlit as st
from PIL import Image

st.title("Welcome to Miss Minutes Meeting Manager!")
st.header("Brought to you by the letter M, and Phil")


miss_min1 = Image.open("miss_minute1.png")
st.image(miss_min1, caption="Let Miss Minutes Do the Minding!")

fields = {
    "time_zone": 0,
    "working_hours_start": 0,
    "working_hours_end": 0,
    "heads_down_time_start": 0,
    "heads_down_time_end": 0,
}


for key, value in fields.items():
    if key not in st.session_state:
        st.session_state[key] = value
