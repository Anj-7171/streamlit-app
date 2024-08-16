import streamlit as st

# title
st.title("My first App")

# text input
name = st.text_input("Enter your name:")
st.write("Hello,", name)

# button
if st.button("Submit"):
    st.write("Congratulation! your srteamlit app is ready")
