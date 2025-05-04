import streamlit as st
import pandas as pd
import joblib

# Load your trained XGBoost model
model = joblib.load('xgb_model.pkl')

st.title("NSE Stock Price Prediction App")
st.subheader("Enter technical indicators to predict the next 'Day Price'")

# User inputs for each feature
low_12m = st.number_input("12-Month Low")
high_12m = st.number_input("12-Month High")
day_low = st.number_input("Day Low")
day_high = st.number_input("Day High")
previous = st.number_input("Previous Close Price")
change = st.number_input("Price Change")
change_pct = st.number_input("Change Percentage")
volume = st.number_input("Volume")
sma_10 = st.number_input("SMA 10")
sma_50 = st.number_input("SMA 50")
ema_10 = st.number_input("EMA 10")
ema_50 = st.number_input("EMA 50")
rsi = st.number_input("RSI")

# When user clicks 'Predict'
if st.button("Predict Day Price"):
    input_data = pd.DataFrame({
        '12m Low': [low_12m],
        '12m High': [high_12m],
        'Day Low': [day_low],
        'Day High': [day_high],
        'Previous': [previous],
        'Change': [change],
        'Change%': [change_pct],
        'Volume': [volume],
        'SMA_10': [sma_10],
        'SMA_50': [sma_50],
        'EMA_10': [ema_10],
        'EMA_50': [ema_50],
        'RSI': [rsi]
    })

    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Day Price: {prediction:.2f}")