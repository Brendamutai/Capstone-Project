import streamlit as st
import pandas as pd
import numpy as np
import joblib
import xgboost as xgb

# Load model and features
model = joblib.load("xgb_model.pkl")
st.title("📈 XGBoost NSE Stock Price Predictor")

# Input: select stock code
stock_code = st.selectbox("Select a Stock Code", options=['EGAD', 'KUKZ', 'KAPC', 'LIMT', 'SASN', 'WTK', 'CGEN', 'ABSA',
 'BKG', 'COOP', 'DTK', 'EQTY', 'HFCK', 'IMH', 'KCB', 'NBK', 'NCBA',
 'SBIC', 'SCBK', 'DCON', 'EVRD', 'XPRS', 'HBE', 'KQ', 'LKL', 'NBV',
 'NMG', 'SMER', 'SGL', 'TPSE', 'UCHM', 'SCAN', 'ARM', 'BAMB',
 'CRWN', 'CABL', 'PORT', 'KEGN', 'KPLC-P4', 'KPLC-P7', 'KPLC',
 'TOTL', 'UMME', 'BRIT', 'CIC', 'JUB', 'KNRE', 'LBTY', 'SLAM',
 'CTUM', 'HAFR', 'KURV', 'OCH', 'TCL', 'NSE', 'BOC', 'BAT', 'CARB',
 'EABL', 'FTGH', 'ORCH', 'MSC', 'UNGA', 'SCOM', 'LAPR', 'GLD',
 '^N10I', '^N20I', '^N25I', '^NASI', '^ZKEQTK', '^ZKEQTU', '^NBDI',
 'HFCK-R']
)
feaute_columns = ['Day Low', 'Day High', 'Previous']
# Input: feature values
st.subheader("Enter feature values:")
input_data = {}
for feature in feature_columns:
    input_data[feature] = st.number_input(f"{feature}", value=0.0)

# Predict button
if st.button("Predict Price"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)
    st.success(f"Predicted Stock Price: {prediction[0]:.2f}")
