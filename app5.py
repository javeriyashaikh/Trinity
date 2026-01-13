import streamlit as st 
import google.generativeai as genai 

st.title("Welcome to the streamlit application")
user_input = st.text_input("ASK ME ANYTHING")

genai.configure(api_key="AIzaSyDYxUOBV8MEy5TyWrCNQzAxX09v6Bsg4l0")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("response", response.text)