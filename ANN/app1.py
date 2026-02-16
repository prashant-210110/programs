import streamlit as st
import tensorflow as tf
import pickle
import pandas as pd

# Load model
model = tf.keras.models.load_model("model.h5")

# Load encoders
with open("labelencoder.pkl", "rb") as f:
    encoder = pickle.load(f)
with open("onehot_encoder_geo.pkl", "rb") as f:
    onehot_encoder_geo = pickle.load(f)

st.title("Customer Churn Prediction App")

# Use categories_ for dropdowns
geography = st.selectbox('Geography', onehot_encoder_geo.categories_[0])
gender = st.selectbox('Gender', encoder.classes_)
age = st.slider('Age', 18, 92)
balance = st.number_input('Balance')
credit_score = st.number_input('Credit Score')
estimated_salary = st.number_input('Estimated Salary')
tenure = st.slider('Tenure', 0, 10)
num_of_products = st.slider('Number of Products', 1, 4)
has_cr_card = st.selectbox('Has Credit Card', [0, 1])
is_active_member = st.selectbox('Is Active Member', [0, 1])

# Prepare input data
input_data = pd.DataFrame({
    "CreditScore": [credit_score],
    "Gender": [encoder.transform([gender])[0]],  # Encode gender
    "Age": [age],
    "Tenure": [tenure],
    "Balance": [balance],
    "NumOfProducts": [num_of_products],
    "HasCrCard": [has_cr_card],
    "IsActiveMember": [is_active_member],
    "EstimatedSalary": [estimated_salary]
})

# Encode geography properly
geo_encoded = onehot_encoder_geo.transform([[geography]])
geo_encoded_df = pd.DataFrame(
    geo_encoded,
    columns=onehot_encoder_geo.get_feature_names_out(onehot_encoder_geo.feature_names_in_)
)

input_data = pd.concat([input_data.reset_index(drop=True), geo_encoded_df], axis=1)

prediction = model.predict(input_data)
prediction_proba = prediction[0][0]

st.write(f'Churn Probability: {prediction_proba:.2f}')
if st.button("Predict"):
    if prediction_proba > 0.5:
        st.write('The customer is likely to churn.')
    else:
        st.write('The customer is not likely to churn.')
