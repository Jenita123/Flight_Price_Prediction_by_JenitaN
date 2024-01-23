import streamlit as st
import pandas as pd

# Title of the app
st.title('Flight Data Viewer')

# Path to your CSV file
file_path = 'datasets/Clean_Dataset.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Display the dataframe
st.write(df)
