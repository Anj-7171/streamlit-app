import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Create sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# Title of the app
st.title("Different Chart Types with Streamlit")

# Line Chart
st.subheader("Line Chart")
st.line_chart(chart_data)

# Area Chart
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Scatter Plot
st.subheader("Scatter Plot")
# Using the first two columns for the scatter plot
st.scatter_chart(chart_data[['a', 'b']])

data = np.random.randn(1000)

st.title("Histogram Example with Matplotlib")
st.subheader("Distribution of Random Data")

# Create a histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title("Histogram of Random Data")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Display the histogram
st.pyplot(plt)
# Data for pie chart
labels = ['A', 'B', 'C', 'D']
sizes = [15, 30, 45, 10]

st.title("Pie Chart Example")
st.subheader("Proportions of Categories")

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%')
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
st.pyplot(fig)


import seaborn as sns

# Generate random data
data = np.random.randn(100)

st.title("Box Plot Example")
st.subheader("Distribution of Random Data")

# Create a box plot
fig, ax = plt.subplots()
sns.boxplot(data=data, ax=ax)
st.pyplot(fig)


data = {
    'City': ['New Delhi', 'Mumbai', 'Bengaluru', 'Chennai', 'Kolkata'],
    'lat': [28.6139, 19.0760, 12.9716, 13.0827, 22.5726],  
    'lon': [77.2090, 72.8777, 77.5946, 80.2707, 88.3639]  
}

# Create DataFrame
locations = pd.DataFrame(data)

# Display the map with the city locations
st.title("Map of India")
st.map(locations[['lat', 'lon']])  # Use the renamed columns