import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Load vectorizer and model
vectorizer = pickle.load(open('countvectorizer.pkl', 'rb'))
model = pickle.load(open('spamhammodel.pkl', 'rb'))

stemmer = PorterStemmer()

def preprocess_text(text):
    review = re.sub('[^a-zA-Z]', ' ', text)
    review = review.lower()
    review = review.split()
    review = [stemmer.stem(word) for word in review if word not in stopwords.words('english')]
    return ' '.join(review)

# Streamlit UI
st.title("📩 Spam Classifier App")
st.write("Enter a message below to check if it's **Ham** or **Spam**.")

user_input = st.text_area("Message:", "")

if st.button("Classify"):
    if user_input.strip() != "":
        processed_text = preprocess_text(user_input)
        vectorized_text = vectorizer.transform([processed_text]).toarray()
        prediction = model.predict(vectorized_text)[0]
        
        if prediction == 'spam' or prediction == 1:
                st.error("🚨 This message is classified as **Spam**")
        else:
             st.success("✅ This message is classified as **Ham**")

    else:
        st.warning("Please enter a message to classify.")
