import streamlit as st 
st.title("Some basic commands in Streamlit")

name = st.text_input("enter your name")

if st.button("submit"):
    st.write("hello", name)
