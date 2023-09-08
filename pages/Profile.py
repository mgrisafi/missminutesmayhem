import streamlit as st
from datetime import datetime


st.title("Miss Minutes Meeting Management")

with st.form("Miss Minutes Meeting Management"):
    # input for timezone
    timezone = st.text_input("Enter your timezone (e.g., GMT+2):")

    # input for working hours
    working_hours_start = st.time_input("Working Hours Start Time:", value=datetime(1, 1, 1, 9, 0).time())
    working_hours_end = st.time_input("Working Hours End Time:", value=datetime(1, 1, 1, 17, 0).time())

    # input for heads-down time 
    heads_down_start = st.time_input("Heads-Down Start Time:", value=datetime(1, 1, 1, 12, 0).time())
    heads_down_end = st.time_input("Heads-Down End Time:", value=datetime(1, 1, 1, 13, 0).time())

    # Radio for location (remote or local)
    location = st.radio("Select your location:", ("Remote", "Local"))

    # input for preferred meeting time
    meeting_start = st.time_input("Preferred Meeting Start Time:", value=datetime(1, 1, 1, 10, 0).time())
    meeting_end = st.time_input("Preferred Meeting End Time:", value=datetime(1, 1, 1, 12, 0).time())

    # Submit 
    submit_button = st.form_submit_button(label="Submit")

# displays input after submission
if submit_button:
    st.success("User Preferences Submitted!")
    st.write("Timezone:", timezone)
    st.write("Working Hours:", working_hours_start.strftime("%I:%M %p"), "to", working_hours_end.strftime("%I:%M %p"))
    st.write("Heads-Down Time:", heads_down_start.strftime("%I:%M %p"), "to", heads_down_end.strftime("%I:%M %p"))
    st.write("Location:", location)
    st.write("Preferred Meeting Time:", meeting_start.strftime("%I:%M %p"), "to", meeting_end.strftime("%I:%M %p"))
