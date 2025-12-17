'''import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("house_price_model.pkl")

# App title
st.title(" House Price Prediction App")

st.write("Enter the details below to predict the house price:")

# User input fields
bedrooms = st.number_input("Number of Bedrooms", min_value=0, max_value=10, value=3)
bathrooms = st.number_input("Number of Bathrooms", min_value=0, max_value=10, value=2)
sqft_living = st.number_input("Sqft Living Area", min_value=100, max_value=10000, value=1800)
sqft_lot = st.number_input("Sqft Lot Area", min_value=100, max_value=50000, value=4000)
sqft_basement = st.number_input("Sqft Basement (optional)", min_value=0, max_value=5000, value=0)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025, value=2005)
yr_renovated = st.number_input("Year Renovated (optional)", min_value=0, max_value=2025, value=0)

# When user clicks button
if st.button("🔍 Predict Price"):
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'sqft_lot': [sqft_lot],
        'sqft_basement': [sqft_basement],
        'yr_built': [yr_built],
        'yr_renovated': [yr_renovated]
    })

    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated House Price: ${prediction:,.2f}")'''
import streamlit as st
import pandas as pd
import joblib

# Page layout
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load model
model = joblib.load("house_price_model.pkl")

# Title & subtitle
st.markdown(
    """
    <h2 style='text-align:center;'>🏠 House Price Prediction</h2>
    <p style='text-align:center;color:gray;'>
    Enter house details to estimate the market price
    </p>
    """,
    unsafe_allow_html=True
)

# Card container
with st.container():

    # Arrange inputs in 2-column layout
    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.number_input("Bedrooms", 0, 10, 3)
        bathrooms = st.number_input("Bathrooms", 0, 10, 2)
        sqft_living = st.number_input("Sqft Living", 100, 10000, 1800)
        sqft_basement = st.number_input("Basement Sqft", 0, 5000, 0)

    with col2:
        sqft_lot = st.number_input("Sqft Lot", 100, 50000, 4000)
        yr_built = st.number_input("Year Built", 1800, 2025, 2005)
        yr_renovated = st.number_input("Renovated Year", 0, 2025, 0)

    st.markdown("<br>", unsafe_allow_html=True)

    # Centered button
    predict = st.button("🔍 Predict Price", use_container_width=True)

# Prediction logic
if predict:
    input_data = pd.DataFrame({
        'bedrooms': [bedrooms],
        'bathrooms': [bathrooms],
        'sqft_living': [sqft_living],
        'sqft_lot': [sqft_lot],
        'sqft_basement': [sqft_basement],
        'yr_built': [yr_built],
        'yr_renovated': [yr_renovated]
    })

    prediction = model.predict(input_data)[0]

    # Result display
    st.markdown("<br>", unsafe_allow_html=True)
    st.success(
        f"💰 **Estimated House Price:** ${prediction:,.2f}",
        icon="✅"
    )
