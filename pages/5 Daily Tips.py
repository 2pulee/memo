import streamlit as st
tab1, tab2 = st.tabs(["How to start a day", "Daily Proverb"])

with tab1:
    st.subheader("How to start a day", divider='red')
    text_object='''Grab a book, newspaper or magazine and start reading today, to:
1. Concentrate better.
2. Emphathize with others better.
3. Keep you brain young.
4. Improve your overall brain health.'''
    st.markdown(text_object)
    st.image('https://media.fuzia.com/assets/uploads/images/co_brand_1/article/2020/fb_img_1579141721190-zs4Y8nMiAWogOQW5.jpg', width=600)

with tab2:
    st.subheader("Proverb Gallery", divider='red')
    import streamlit as st

    col1, col2, col3 = st.columns(3)

    with col1:
     st.subheader("Day 1")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Productivity-isnt-about-being-a-workhorse.-Keeping-busy-or-burning-the-midnight-oil%E2%80%A6-Its-more-about-priorities-planning-and-fiercely-protecting-your-time.-Gary-Keller.jpg")

    with col2:
     st.subheader("Day 2")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/I-think-of-productivity-as-using-your-time-to-accomplish-things-of-value-to-you-and-others.-Adam-Grant.jpg")

    with col3:
     st.subheader("Day 3")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")
    
    col4, col5, col6 = st.columns(3)

    with col4:
     st.subheader("Day 4")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")

    with col5:
     st.subheader("Day 5")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")

    with col6:
     st.subheader("Day 6")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")

    col7, col8, col9 = st.columns(3)

    with col7:
     st.subheader("Day 7")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")

    with col8:
     st.subheader("Day 8")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")

    with col9:
     st.subheader("Day 9")
     st.image("https://cdn.graciousquotes.com/wp-content/uploads/2021/11/Doing-less-is-not-being-lazy.-Dont-give-in-to-a-culture-that-values-personal-sacrifice-over-personal-productivity.-Tim-Ferriss.jpg")