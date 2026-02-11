import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import matplotlib.pyplot as plt

st.title("🏠 House Price Prediction using ANN")

# File uploader
uploaded_file = st.file_uploader("Upload House Price CSV", type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("### Raw Data Preview")
    st.dataframe(data.head())

    # Handle missing values
    data.fillna(data.mean(numeric_only=True), inplace=True)

    # Encode categorical features
    for col in data.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        data[col] = le.fit_transform(data[col].astype(str))

    # Split features and target
    X = data.drop("Price_in_Lakhs", axis=1)
    y = data["Price_in_Lakhs"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Feature scaling
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Hyperparameters from sidebar
    st.sidebar.header("Model Parameters")
    epochs = st.sidebar.slider("Epochs", 50, 500, 100, step=50)
    batch_size = st.sidebar.selectbox("Batch Size", [16, 32, 64, 128])

    # Build ANN
    model = Sequential([
        Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(32, activation='relu'),
        Dense(1, activation='linear')
    ])

    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])

    # Train model
    history = model.fit(
        X_train, y_train,
        epochs=epochs,
        batch_size=batch_size,
        validation_split=0.2,
        verbose=0
    )

    # Evaluate
    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    st.write(f"### Test MAE: {mae:.2f}")

    # Plot training history
    st.write("### Training History")
    fig, ax = plt.subplots()
    ax.plot(history.history['loss'], label='Train Loss')
    ax.plot(history.history['val_loss'], label='Validation Loss')
    ax.set_xlabel("Epochs")
    ax.set_ylabel("Loss")
    ax.legend()
    st.pyplot(fig)

    # Predictions
    y_pred = model.predict(X_test)
    st.write("### Sample Predictions")
    st.write(pd.DataFrame({"Actual": y_test[:10].values, "Predicted": y_pred[:10].flatten()}))
