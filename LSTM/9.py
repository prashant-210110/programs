import streamlit as st
import numpy as np
import pandas as pd
import pickle
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(page_title="Google Stock Predictor", layout="wide")
st.title("📈 Google Stock Price Prediction (LSTM)")

# -----------------------------
# Load Model and Scaler
# -----------------------------
@st.cache_resource
def load_assets():
    with open("lstm_model.pkl", "rb") as f:
        model = pickle.load(f)
    scaler = joblib.load("scaler.pkl")
    return model, scaler

model, scaler = load_assets()

# -----------------------------
# Sidebar Navigation
# -----------------------------
st.sidebar.header("Navigation")
option = st.sidebar.radio("Choose Input Method", ["Manual Entry", "CSV Upload"])

# -----------------------------
# Manual Entry with Sliders
# -----------------------------
if option == "Manual Entry":

    st.subheader("Select Last 10 Days Open Prices (Slider Input)")

    cols = st.columns(5)
    input_prices = []

    for i in range(10):
        with cols[i % 5]:
            price = st.slider(
                f"Day {i+1}",
                min_value=100.0,
                max_value=500.0,
                value=300.0,
                step=0.1,
                key=f"slider_{i}"
            )
            input_prices.append(price)

    st.write("Selected Prices:", input_prices)

    # Prediction Button
    if st.button("Predict Next Day Price"):

        data = np.array(input_prices).reshape(-1, 1)
        scaled_data = scaler.transform(data)

        X_test = np.reshape(scaled_data, (1, 10, 1))

        prediction = model.predict(X_test)
        predicted_price = scaler.inverse_transform(prediction)

        st.success(f"### Predicted Next Day Price: ${predicted_price[0][0]:.2f}")

# -----------------------------
# CSV Upload Prediction
# -----------------------------
else:

    st.subheader("Batch Prediction via CSV")
    st.info("Upload a CSV file containing at least 10 rows of 'Open' prices.")

    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.write("Preview of Uploaded Data:", df.head())

        if 'Open' in df.columns:

            if len(df) >= 10:

                last_10_days = df['Open'].tail(10).values.reshape(-1, 1)

                scaled_data = scaler.transform(last_10_days)
                X_test = np.reshape(scaled_data, (1, 10, 1))

                if st.button("Predict from CSV"):

                    prediction = model.predict(X_test)
                    predicted_price = scaler.inverse_transform(prediction)

                    st.success(f"### Predicted Price based on CSV: ${predicted_price[0][0]:.2f}")

            else:
                st.error("CSV must have at least 10 rows of data.")

        else:
            st.error("CSV must contain an 'Open' column.")