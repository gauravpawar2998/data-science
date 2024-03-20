
import streamlit as st
import joblib
import pandas as pd 

st.image("oil-price-predictions.png",channels='RGB',output_format="PNG")

# Load the saved Random Forest model
model = joblib.load('random_forest_model_save14.pkl')

st.header('Oil Price Prediction Day Wise',divider='rainbow')

# Input features for prediction

st.text("Enter the Value for Year, Month, Day")
year = st.number_input('Year', value=2023)
month = st.number_input('Month', min_value=1, max_value=12, value=1)
day = st.number_input('Day', min_value=1, max_value=31, value=1)
Volume = 100000

# Make a prediction
prediction_data = {'Year': [year], 'Month': [month], 'Day': [day], 'Volume': [Volume]}
input_df = pd.DataFrame(prediction_data)
prediction = model.predict(input_df)

st.write('Predicted Oil Price:', prediction[0])

# Information
st.info(
    "This Streamlit app presents the entire Oil Price Prediction project. "
    "It includes data preprocessing, exploratory data analysis (EDA)"
    "Adjust the settings in the sidebar to predict future oil prices using Random Forest Day wise Oil price."
)


st.header('_Streamlit_ is :blue[cool] :sunglasses:')
