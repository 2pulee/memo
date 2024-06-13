import streamlit as st
title = st.header("📋 Daily Routine Check-List")


task1 = st.checkbox("Go to the Gym")
task2 = st.checkbox("Drink 1L of Water")
task3 = st.checkbox("Read 10 pages of Book")

if task1:
    st.write("Great!")

if task2:
    st.write("Awesome!")

if task3:
    st.write("Look at you!")

st.title=("To-Do List")

task = st.text_input("Enter your task", " ")

if st.button("Add Task"):
    if task:
        st.session_state["task_list"].append(task)

if "task_list" not in st.session_state:
        st.session_state["task_list"] = []

for i, t in enumerate(st.session_state["task_list"]):
    st.write(f"{i+1}. {t}")

for i, t in enumerate(st.session_state["task_list"]):
   if st.checkbox(f"{i+1}. t") : 
    st.session_state["task_list"].remove(t)