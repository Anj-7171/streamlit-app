import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# Title and Header
st.title("Interactive Streamlit App")
st.header("Welcome to My App!")

# Text Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

#Text area
message = st.text_area("Enter your message:")
if message:
    st.write("Your message:", message)

# Slider
age = st.slider("Select your age:", 0, 100, 25)
st.write("Your age is:", age)

# Button
if st.button("Submit"):
    st.write("Button clicked!")

# Checkbox
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

# Radio Buttons
option = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Select Box
fruit = st.selectbox("Select a fruit:", ["Apple", "Banana", "Cherry"])
st.write("You selected:", fruit)

#Multi select
options = st.multiselect("Choose your favorite fruits:", ["Apple", "Banana", "Cherry", "Date"])
st.write("You selected:", options)

#Color picker
color = st.color_picker("Pick a color", "#00f900")
st.write("Selected color:", color)


# DataFrame
data = {
    "Column 1": [1, 2, 3],
    "Column 2": [4, 5, 6]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Line Chart
x = np.linspace(0, 10, 100)
y = np.sin(x)
st.line_chart(y)

#Date input 

import datetime

date = st.date_input("Select a date", datetime.date.today())
st.write("Selected date:", date)


#Time input
#time = st.time_input("Select a time", datetime.time(8, 0))
#st.write("Selected time:", time)

#File uploader
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)

# Image
image = Image.open("logo.jpg")
st.image(image, caption='Streamlit Logo', use_column_width=True)

#image uploader
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image.", use_column_width=True)

#Progress bar

import time
selected_time = st.time_input("Select a time", datetime.time(8, 0))
st.write("Selected time:", selected_time)

# Progress Bar Example
st.write("Progress Bar Example")
progress = st.progress(0)

#Spinner

with st.spinner("Wait for it..."):
    time.sleep(10)  
st.success("Done!")

#Expander
with st.expander("See explanation"):
    st.write("Here is the explanation...")

#Columns
col1, col2 = st.columns(2)
col1.write("Column 1")
col2.write("Column 2")

