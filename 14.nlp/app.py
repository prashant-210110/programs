import streamlit as st
import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download stopwords if not already
nltk.download('stopwords')

# Load dataset
df = pd.read_csv(r"c:\DATA SCIENCE\Machine_Learning\Datasets\data.csv")

# Preprocessing
stemmer = PorterStemmer()
corpus = []
for i in range(len(df)):
    review = re.sub('[^a-zA-Z]', ' ', df['Sentence'][i])
    review = review.lower()
    review = review.split()
    review = [stemmer.stem(word) for word in review if word not in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)

# Encode labels
le = LabelEncoder()
df["Sentiment"] = le.fit_transform(df["Sentiment"])

# Train/test split
x = corpus
y = df["Sentiment"].values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
x_train = vectorizer.fit_transform(x_train)
x_test = vectorizer.transform(x_test)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(x_train, y_train)

# Accuracy
accuracy = accuracy_score(y_test, model.predict(x_test))

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
    return "negative" if prediction == 1 else "positive", confidence

# Streamlit UI
st.title("🎬 Movie Review Sentiment Analysis")
st.write("This app predicts whether a movie review is **positive** or **negative** using Logistic Regression.")

st.sidebar.header("Model Info")
st.sidebar.write(f"Accuracy on test set: **{accuracy:.2f}**")

review = st.text_area("Enter your movie review:")

if st.button("Predict Sentiment"):
    if review.strip():
        sentiment, confidence = predict_sentiment(review)
        st.success(f"Prediction: **{sentiment}** (Confidence: {confidence:.2f}%)")
    else:
        st.warning("⚠ Please enter a review first.")
