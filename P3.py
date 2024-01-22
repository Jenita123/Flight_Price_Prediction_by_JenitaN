import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the app
st.title('Flight Data Viewer')

# Path to your CSV file
file_path = 'datasets/Clean_Dataset.csv'

# Read the CSV file
df = pd.read_csv(file_path)

# Sidebar for filters
st.sidebar.header('Filter Options')

# Selectbox for airline company
selected_airline = st.sidebar.selectbox('Select Airline Company', options=['All']+list(df['airline'].unique()))

# Selectbox for source city
selected_source = st.sidebar.selectbox('Select Source City', options=['All']+list(df['source_city'].unique()))

# Selectbox for destination city
selected_destination = st.sidebar.selectbox('Select Destination City', options=['All']+list(df['destination_city'].unique()))

# Filtering the dataframe
if selected_airline != 'All':
    df = df[df['airline'] == selected_airline]

if selected_source != 'All':
    df = df[df['source_city'] == selected_source]

if selected_destination != 'All':
    df = df[df['destination_city'] == selected_destination]

# Display the filtered dataframe
st.write("Filtered Data", df)

# Display summary statistics
st.write("Summary Statistics", df.describe())

# Visualization Section
st.header("Data Visualizations")

# Number of flights per airline
if 'airline' in df.columns:
    st.subheader("Number of Flights Per Airline")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x='airline', ax=ax)
    st.pyplot(fig)

# Distribution of flight duration
if 'duration' in df.columns:
    st.subheader("Flight Duration Distribution")
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='duration', kde=True, ax=ax)
    st.pyplot(fig)
