import streamlit as st
from datetime import datetime

st.title("Miss Minutes Meeting Manager")

with st.form("Miss Minutes Meeting Manager"):
    
    # input for timezone
    timezone = st.text_input("Enter your timezone (e.g., PDT):")
    
    # Radio for location (remote or local)
    location = st.radio("Select your location:", ("Remote", "Local"))

    # input for working hours
    st.write("Working Hours:")
    working_hours_start = st.time_input("Start Time:", value=datetime(1, 1, 1, 9, 0).time())
    working_hours_end = st.time_input("End Time:", value=datetime(1, 1, 1, 17, 0).time())

    # input for heads-down time
    st.write("Heads-Down Time:")
    heads_down_start = st.time_input("Start Time:", value=datetime(1, 1, 1, 12, 0).time())
    heads_down_end = st.time_input("End Time:", value=datetime(1, 1, 1, 13, 0).time())

    # input for preferred meeting time
    st.write("Preferred Meeting Time:")
    meeting_start = st.time_input("Start Time:", value=datetime(1, 1, 1, 10, 0).time())
    meeting_end = st.time_input("End Time:", value=datetime(1, 1, 1, 12, 0).time())

    # Submit
    submit_button = st.form_submit_button(label="Submit")


if submit_button:
    if working_hours_start >= working_hours_end:
        st.error("Working hours end time must be after start time.")
    elif not timezone:
        st.error("Please enter your timezone.")
    else:
        st.success("Meeting preferences saved!")
        st.write("Timezone:", timezone)
        st.write("Working Hours:", working_hours_start.strftime("%I:%M %p"), "to", working_hours_end.strftime("%I:%M %p"))
        st.write("Heads-Down Time:", heads_down_start.strftime("%I:%M %p"), "to", heads_down_end.strftime("%I:%M %p"))
        st.write("Location:", location)
        st.write("Preferred Meeting Time:", meeting_start.strftime("%I:%M %p"), "to", meeting_end.strftime("%I:%M %p"))
