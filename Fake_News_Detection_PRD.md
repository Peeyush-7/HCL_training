# Product Requirements Document (PRD)

## Fake News Detection Using NLP

**Version:** 1.0\
**Project Type:** Academic ML/NLP Project\
**Frontend:** Streamlit\
**Backend/Model:** Python + Scikit-learn

------------------------------------------------------------------------

## 1. Product Overview

The system will allow users to enter or paste a news article into a
Streamlit web interface. The application will preprocess the text,
convert it into numerical NLP features, and use a trained
machine-learning model to classify the news as **Fake** or **Real**.

### Basic Flow

``` text
User
  ↓
Streamlit UI
  ↓
News Text
  ↓
Text Preprocessing
  ↓
TF-IDF Feature Extraction
  ↓
ML Classification Model
  ↓
Fake / Real Prediction
```

------------------------------------------------------------------------

## 2. Objectives

### Primary Objectives

-   Build an NLP-based fake news classification system.
-   Clean and preprocess news text.
-   Convert text into numerical features using TF-IDF.
-   Train and evaluate machine-learning classification models.
-   Select an appropriate model based on evaluation metrics.
-   Develop an interactive Streamlit frontend.
-   Display the prediction clearly to the user.

### Success Criteria

-   Successfully classify unseen news articles.
-   Achieve reasonable classification performance on the selected
    dataset.
-   Provide a simple and understandable UI.
-   Allow users to test multiple news articles without restarting the
    application.

------------------------------------------------------------------------

## 3. Target Users

**Primary User:** Students and general users who want to test whether a
piece of news is classified as fake or real.

> The system is intended as an ML demonstration/educational tool, not as
> a definitive fact-checking authority.

------------------------------------------------------------------------

## 4. Functional Requirements

### FR1 --- News Input

-   Provide a text area where the user can paste or enter news content.
-   Optionally support a separate news headline and article/body input.

### FR2 --- Text Preprocessing

The system shall perform appropriate preprocessing, including:

-   Lowercase conversion
-   Removal of unnecessary characters
-   URL removal
-   Punctuation handling
-   Stopword handling
-   Tokenization
-   Lemmatization or stemming where appropriate

### FR3 --- Feature Extraction

The system shall use **TF-IDF Vectorization** to convert processed text
into numerical features.

### FR4 --- Classification

The system shall:

-   Classify the input as **REAL** or **FAKE**.
-   Compare suitable baseline models such as:
    -   Logistic Regression
    -   Naive Bayes
    -   Support Vector Machine
-   Use the selected best-performing model in the final application.

### FR5 --- Prediction Result

The application shall:

-   Display the prediction clearly.
-   Display a confidence/probability value when the selected model
    provides a meaningful estimate.

Example:

``` text
Prediction: FAKE
Confidence: 94.2%
```

### FR6 --- Model Evaluation

The development process shall evaluate the model using:

-   Accuracy
-   Precision
-   Recall
-   F1 Score
-   Confusion Matrix

------------------------------------------------------------------------

## 5. Streamlit UI Requirements

### Main Page

The application should contain:

-   Application title: **Fake News Detector**
-   Large text area for entering/pasting a news article
-   **Detect News** button
-   Clear prediction result
-   Confidence value when applicable

Example:

``` text
────────────────────────────────────────
          📰 Fake News Detector
────────────────────────────────────────

Enter your news article:

┌──────────────────────────────────────┐
│ Paste news article here...           │
│                                      │
│                                      │
└──────────────────────────────────────┘

          [ 🔍 Detect News ]

────────────────────────────────────────

Prediction: 🔴 FAKE

Confidence: 94.2%
```

### Optional Sidebar

-   About
-   How it works
-   Model Information
-   Evaluation Metrics

------------------------------------------------------------------------

## 6. Non-Functional Requirements

### Usability

-   Simple interface
-   Clear prediction
-   Minimal user interaction
-   Responsive Streamlit layout

### Performance

-   Prediction should complete within a few seconds.
-   Model should be loaded once when the application starts.

### Reliability

-   Handle empty input gracefully.
-   Handle very short or invalid text.
-   Prevent application crashes from unexpected input.

### Maintainability

Keep the following components logically separated:

-   Data preprocessing
-   Model training
-   Prediction
-   Streamlit UI

------------------------------------------------------------------------

## 7. Technical Stack

  Component            Technology
  -------------------- ----------------------------
  Programming          Python
  Data Processing      Pandas, NumPy
  NLP                  NLTK / spaCy
  Feature Extraction   TF-IDF
  Machine Learning     Scikit-learn
  Visualization        Matplotlib / Seaborn
  Frontend             Streamlit
  Model Storage        Joblib / Pickle
  Development          Jupyter Notebook / VS Code
  Version Control      Git + GitHub

------------------------------------------------------------------------

## 8. Project Deliverables

### D1 --- Dataset

Cleaned and prepared fake/real news dataset.

### D2 --- NLP Pipeline

Text preprocessing and TF-IDF implementation.

### D3 --- ML Models

Multiple baseline models trained and evaluated.

### D4 --- Final Model

Selected classification model saved for application use.

### D5 --- Streamlit Application

Working web interface for real-time prediction.

### D6 --- Documentation

-   README
-   Project report
-   Model evaluation results
-   Setup instructions

------------------------------------------------------------------------

## 9. MVP Scope

The **Minimum Viable Product (MVP)** will contain:

``` text
Dataset
   ↓
Preprocessing
   ↓
TF-IDF
   ↓
ML Model
   ↓
Evaluation
   ↓
Save Model
   ↓
Streamlit UI
   ↓
User Input
   ↓
Fake / Real Prediction
```

### Not Included in MVP

-   Live news scraping
-   Social media analysis
-   Real-time fact checking
-   External fact-checking APIs
-   BERT/RoBERTa
-   User authentication
-   Database
-   Mobile application

------------------------------------------------------------------------

## 10. Scrum Backlog

  Sprint         Tasks                                   Priority
  -------------- --------------------------------------- ----------
  **Sprint 1**   Dataset selection, EDA, data cleaning   High
  **Sprint 2**   NLP preprocessing + TF-IDF              High
  **Sprint 3**   Train & compare ML models               High
  **Sprint 4**   Evaluation + save final model           High
  **Sprint 5**   Build Streamlit UI                      High
  **Sprint 6**   Integrate model + UI testing            High
  **Sprint 7**   Documentation, report, final demo       Medium

### Definition of Done

A task is considered complete when:

-   Code runs without errors.
-   Output is verified.
-   Changes are committed to Git.
-   Relevant documentation is updated.

------------------------------------------------------------------------

## 11. Future Enhancements

Possible future additions include:

-   Headline + article analysis
-   Multiple model selection
-   Prediction history
-   Visualization dashboard
-   Explainable predictions
-   Transformer-based models
-   Integration with trusted fact-checking sources

> **Recommended scope:** Build the MVP first, then add only 1--2
> enhancements if time permits. This keeps the project manageable while
> still providing a polished final demonstration.
