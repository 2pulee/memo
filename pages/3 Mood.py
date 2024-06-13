import streamlit as st

st.set_page_config(layout="wide")

st.header('🙂 Record Your Mood 🍔')

with st.expander('About this feature'):
  st.write('This fuction is made for yourself to record your daily mood & food.')
  st.image('https://static.vecteezy.com/system/resources/previews/007/802/611/non_2x/emotion-levels-on-the-scale-of-different-faces-icon-design-element-for-feedback-review-rating-product-review-set-emoji-with-different-emotions-on-white-background-illustration-vector.jpg', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Select Emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What did you eat?', ['', 'Ramyeon', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3)

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Insert your **name**!')

with col2:
  if user_emoji != '':
    st.write(f"You're feeling {user_emoji}")
  else:
    st.write('👈 Select your **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 You should eat **{user_food}** today!')
  else:
    st.write('👈 Select **food** for today!')
