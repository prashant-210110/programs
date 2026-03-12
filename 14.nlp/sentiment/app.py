import streamlit as st
import pickle
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('stopwords')
stemmer = PorterStemmer()

# Load pickled objects
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("labelencoder.pkl", "rb") as f:
    le = pickle.load(f)

# Prediction function
def predict_sentiment(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [stemmer.stem(word) for word in review if word not in stopwords.words('english')]
    review = ' '.join(review)
    vectorized = vectorizer.transform([review])
    prediction = model.predict(vectorized)[0]
    probability = model.predict_proba(vectorized)[0]
    confidence = max(probability) * 100
    # Decode numeric prediction back to original label
    sentiment_label = le.inverse_transform([prediction])[0]
    return sentiment_label, confidence

# Streamlit UI
st.title("🎬 Movie Review Sentiment Analysis")
st.write("This app predicts whether a movie review is **positive** or **negative** using a pre-trained Logistic Regression model.")

review = st.text_area("Enter your movie review:")

if st.button("Predict Sentiment"):
    if review.strip():
        sentiment, confidence = predict_sentiment(review)
        st.success(f"Prediction: **{sentiment}** (Confidence: {confidence:.2f}%)")
    else:
        st.warning("⚠ Please enter a review first.")
