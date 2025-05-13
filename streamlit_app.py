import streamlit as st
import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import os
import joblib
import plotly.express as px

# Load feature data
DATA_PATH = 'nse_features_full.csv'
df = pd.read_csv(DATA_PATH)
stocks = df['Code'].unique()

# Streamlit UI
st.title("📈 NSE Stock Price Predictor")

selected_stock = st.selectbox("Choose a stock ticker:", sorted(stocks))

# Filter and sort data
stock_data = df[df['Code'] == selected_stock].copy()
stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')
stock_data = stock_data.sort_values(by='Date')

# Define cutoff date
N_DAYS = 30
latest_date = stock_data['Date'].max()
cutoff_date = latest_date - pd.Timedelta(days=N_DAYS)

# Filter for last N days and aggregate by date
trend_data = (
    stock_data[stock_data['Date'] >= cutoff_date]
    .groupby('Date', as_index=False)['Day Price']
    .mean()
)

# Layout: Tabs for Trend and Prediction
tab1, tab2 = st.tabs(["Recent Price Trend", "Predict Next Price"])

# Tab 1: Price Trend
with tab1:
    st.subheader(f"{selected_stock} - Interactive Price Trend")

    max_days = (stock_data['Date'].max() - stock_data['Date'].min()).days
    N_DAYS = st.slider("Select how many past days to show", min_value=7, max_value=max(30, max_days), value=30)

    latest_date = stock_data['Date'].max()
    cutoff_date = latest_date - pd.Timedelta(days=N_DAYS)
    trend_data = stock_data[stock_data['Date'] >= cutoff_date][['Date', 'Day Price']].dropna()

    if not trend_data.empty:
        fig = px.line(
            trend_data,
            x='Date',
            y='Day Price',
            title=f'{selected_stock} Price Trend (Last {N_DAYS} Days)',
            markers=True
        )

        fig.update_layout(
            xaxis_title="Date",
            yaxis_title="Day Price (KES)",
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=7, label="1w", step="day", stepmode="backward"),
                        dict(count=14, label="2w", step="day", stepmode="backward"),
                        dict(count=30, label="1m", step="day", stepmode="backward"),
                        dict(step="all", label="All")
                    ])
                ),
                rangeslider=dict(visible=True),
                type="date"
            )
        )

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Not enough valid data to display a trend.")

# Tab 2: Prediction
with tab2:
    st.subheader("Predict Tomorrow's Price")
    if st.button("Predict"):
        try:
            # Load model and scalers
            model_path = f"saved_models/model_{selected_stock}.keras"
            feature_scaler_path = f"saved_models/feature_scaler_{selected_stock}.pkl"
            target_scaler_path = f"saved_models/target_scaler_{selected_stock}.pkl"

            model = tf.keras.models.load_model(model_path)
            feature_scaler = joblib.load(feature_scaler_path)
            target_scaler = joblib.load(target_scaler_path)

            # Prepare features
            n_steps = 10
            features = stock_data.drop(columns=['index', 'Date', 'Code', 'Name', 'Sector', 'Code_enc', 'Day Price'])
            target = stock_data[['Day Price']]

            # Scale and combine
            feature_scaled = feature_scaler.transform(features)
            target_scaled = target_scaler.transform(target)
            combined = np.hstack([feature_scaled, target_scaled])

            if len(combined) < n_steps:
                st.warning("Not enough data to make prediction.")
            else:
                input_seq = combined[-n_steps:]
                X_input = np.expand_dims(input_seq[:, :-1], axis=0)
                y_pred_scaled = model.predict(X_input)[0][0]
                y_pred = target_scaler.inverse_transform([[y_pred_scaled]])[0][0]

                st.success(f"Predicted Day Price: **{y_pred:.2f} KES**")

        except Exception as e:
            st.error(f"Prediction failed: {e}")
