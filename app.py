import streamlit as st
st.image("hehe.jpg", caption="My Uploaded Image", use_container_width=True)

st.title("My First Streamlit App 🎉")
st.write("This app is running from a simple Python file!")

x = st.slider("Pick a number", 0, 100, 50)
st.write("You selected:", x)


