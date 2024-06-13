import streamlit as st
title = st.header("⏰ Write down your plan for today!")

import datetime

d = st.date_input("Select Date", value=None)

t = st.time_input('Select Time', value=None)
st.write("Your plan is on:", t,d)

# Text submit
plan = st.text_area("What's your plan?", height=200)
save_button = st.button("Save")
if save_button:
    with open("plan.txt", "w", encoding="UTF-8") as file:
     file.write(plan)
     st.success("Your plan is successfully saved.")

st.subheader("Saved plan")
try:
   with open("plan.txt", "r", encoding="UTF-8") as file:
      saved_plan = file.read()
      st.write(saved_plan)
except FileNotFoundError:
   st.info("There is no saved plan.")  