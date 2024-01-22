import streamlit as st
import pandas as pd

# Title of the app
st.title('Flight Data Viewer')

# Path to your CSV file
file_path = 'datasets/Clean_Dataset.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Sidebar for filters
st.sidebar.header('Filter Options')

# Selectbox for airline company
selected_airline = st.sidebar.selectbox('Select Airline Company', options=df['airline'].unique())

# Selectbox for source city
selected_source = st.sidebar.selectbox('Select Source City', options=df['source_city'].unique())

# Selectbox for destination city
selected_destination = st.sidebar.selectbox('Select Destination City', options=df['destination_city'].unique())

# Filter the dataframe based on selected options
filtered_df = df[(df['airline'] == selected_airline) & 
                 (df['source_city'] == selected_source) & 
                 (df['destination_city'] == selected_destination)]

# Display the filtered dataframe
st.write(filtered_df)
