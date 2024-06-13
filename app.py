import streamlit as st

st.header("🗓 What's Your Plan Today?")

st.header("App Description", divider='rainbow')

text_object = '''This app is for recording your daily plan.

You can save your plan into the calendar.

If you click the specific date on calendar, you can see your past plans.

You can also share your daily plans with your friends.

This app can work as a calendar app in your smartphone but it's more convenient & organized to use.'''
st.markdown(text_object)

st.divider()
# Text submit
title = st.header("✏️ Quick Memo Here")
plan = st.text_area("What's your plan?", height=200)
save_button = st.button("Save")
if save_button:
    with open("plan.txt", "w", encoding="UTF-8") as file:
     file.write(plan)
     st.success("Your plan is successfully saved.")

st.subheader("📁 Saved plan")
try:
   with open("plan.txt", "r", encoding="UTF-8") as file:
      saved_plan = file.read()
      st.write(saved_plan)
except FileNotFoundError:
   st.info("There is no saved plan.")  

