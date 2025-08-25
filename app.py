import streamlit as st

st.title("My First Streamlit App 🎉")
st.write("This app is deployed on Streamlit Community Cloud.")
x = st.slider("Pick a number", 0, 100, 42)
st.write("You selected:", x)
