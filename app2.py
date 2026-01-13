import streamlit as st 

st.title("Some basic commands like sliders, buttons, etc in st")
age = st.slider("Enter your age", 1, 100)

city = st.selectbox("Choose your city", ["Mumbai","Delhi","Pune","Bangalore"])

if st.button("show details"):
    st.write("age",age)
    st.write("city",city)