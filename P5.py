import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder

# Load and preprocess the dataset
@st.cache
def load_data(file_path):
    df = pd.read_csv(file_path)
    # Basic preprocessing
    label_encoders = {}
    for column in ['airline', 'source_city', 'destination_city', 'class']:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df, label_encoders

df, label_encoders = load_data('datasets/Clean_Dataset.csv')

# Split the data
X = df[['airline', 'source_city', 'destination_city', 'class']]  # Simple feature set
y = df['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
error = mean_squared_error(y_test, y_pred)

# Streamlit app
st.title('Flight Data Viewer')

# Sidebar for prediction inputs
st.sidebar.header('Price Prediction')
selected_airline = st.sidebar.selectbox('Select Airline', options=df['airline'].unique())
selected_source = st.sidebar.selectbox('Select Source City', options=df['source_city'].unique())
selected_destination = st.sidebar.selectbox('Select Destination City', options=df['destination_city'].unique())
selected_class = st.sidebar.selectbox('Select Class', options=df['class'].unique())

if st.sidebar.button('Predict Price'):
    # Prepare the input for prediction
    input_data = pd.DataFrame([[selected_airline, selected_source, selected_destination, selected_class]])
    # Predict price
    predicted_price = model.predict(input_data)[0]
    st.sidebar.write(f"Predicted Flight Price: ${predicted_price:.2f}")

# Main section for data exploration
st.write("Filtered Data", df)
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
