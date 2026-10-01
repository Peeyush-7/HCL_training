import streamlit as st
import joblib
import re
import string


# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)


# -----------------------------------
# Load Model
# -----------------------------------

@st.cache_resource
def load_models():

    model = joblib.load(
        "models/fake_news_model.pkl"
    )

    vectorizer = joblib.load(
        "models/tfidf_vectorizer.pkl"
    )

    return model, vectorizer


model, vectorizer = load_models()


# -----------------------------------
# Text Preprocessing
# -----------------------------------

def clean_text(text):

    text = str(text)

    text = text.lower()

    text = re.sub(
        r"http\S+|www\S+|https\S+",
        "",
        text
    )

    text = re.sub(
        r"<.*?>",
        "",
        text
    )

    text = text.translate(
        str.maketrans(
            "",
            "",
            string.punctuation
        )
    )

    text = re.sub(
        r"\d+",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        " ",
        text
    ).strip()

    return text


# -----------------------------------
# UI
# -----------------------------------

st.title("📰 Fake News Detector")

st.write(
    "Enter a news article below and the machine-learning "
    "model will classify it as Real or Fake."
)

news_text = st.text_area(
    "Enter News Article",
    height=250,
    placeholder="Paste the news article here..."
)


# -----------------------------------
# Prediction
# -----------------------------------

if st.button(
    "🔍 Detect News",
    use_container_width=True
):

    if not news_text.strip():

        st.warning(
            "Please enter a news article."
        )

    else:

        cleaned = clean_text(
            news_text
        )

        vectorized = vectorizer.transform(
            [cleaned]
        )

        prediction = model.predict(
            vectorized
        )[0]

        probabilities = model.predict_proba(
            vectorized
        )[0]

        confidence = (
            probabilities[prediction] * 100
        )

        if prediction == 0:

            st.success(
                "🟢 Prediction: REAL NEWS"
            )

        else:

            st.error(
                "🔴 Prediction: FAKE NEWS"
            )

        st.metric(
            "Model Confidence",
            f"{confidence:.2f}%"
        )


# -----------------------------------
# Disclaimer
# -----------------------------------

st.divider()

st.caption(
    "This application is an ML-based educational tool. "
    "Its prediction should not be treated as definitive "
    "fact-checking."
)