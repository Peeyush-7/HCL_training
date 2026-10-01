# Fake News Detection Using NLP

A machine-learning based application that classifies a news article as **Real** or **Fake** using Natural Language Processing (NLP), TF-IDF feature extraction, and Logistic Regression.

The project provides an interactive **Streamlit** web interface where users can enter a news article and receive a prediction with a model confidence score.

## Features

- News article text input through a Streamlit interface
- Text preprocessing and normalization
- TF-IDF based feature extraction
- Unigram and bigram features
- Logistic Regression classification
- Real/Fake prediction
- Model confidence display
- Saved model and TF-IDF vectorizer for application inference

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| NLP / Text Processing | Python, regular expressions |
| Feature Extraction | TF-IDF |
| Machine Learning | Scikit-learn |
| Classification Model | Logistic Regression |
| Frontend | Streamlit |
| Model Serialization | Joblib |
| Data Processing | Pandas, NumPy |
| Dataset Format | CSV |

## Dataset

The project uses the **Fake and Real News Dataset**:

`clmentbisaillon/fake-and-real-news-dataset`

The dataset contains separate `True.csv` and `Fake.csv` files.

The project uses:

- `0` → REAL
- `1` → FAKE

For model input, the **news title and article text are combined**.

## Machine Learning Pipeline

```text
True.csv + Fake.csv
        ↓
   Data Cleaning
        ↓
Title + Article Text
        ↓
 Text Preprocessing
        ↓
     TF-IDF
 (Unigrams + Bigrams)
        ↓
Logistic Regression
        ↓
 REAL / FAKE
        ↓
 Confidence Score
```

## Model Configuration

The trained model used by the application is Logistic Regression.

The TF-IDF vectorizer is configured with:

- Maximum features: `50,000`
- N-gram range: `(1, 2)`
- Minimum document frequency: `2`
- Maximum document frequency: `0.95`
- Sublinear TF: `True`

The Logistic Regression model uses:

- Solver: `lbfgs`
- Maximum iterations: `1000`
- `C`: `1.0`
- Random state: `42`

## Project Structure

```text
fake-news-detection/
│
├── app.py
│
├── models/
│   ├── fake_news_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── assets/
│   └── fake-news-detector.png
│
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd fake-news-detection
```

> Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the actual repository URL after creating the GitHub repository.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows:**

```cmd
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## Web Interface

![Fake News Detector Streamlit Interface](assets/fake-news-detector.png)

The interface allows the user to paste a news article and click **Detect News**. The application then displays the predicted class and model confidence.

## Model Files

The application requires the following trained artifacts:

```text
models/fake_news_model.pkl
models/tfidf_vectorizer.pkl
```

These files contain the trained Logistic Regression model and fitted TF-IDF vectorizer used for prediction.

## Important Note

This application is an **ML-based educational project**. Its prediction indicates how the trained model classifies the supplied text and should not be treated as definitive fact-checking or proof that a news article is true or false.

## Project Information

**Project:** Fake News Detection Using Natural Language Processing (NLP)

**Student:** Peeyush Kumar  
**Roll No.:** 2400320100797

**Supervisor:** Ankit Mishra  
**Designation:** Data Scientist

**Academic Year:** 2026–2027
