# 💵 Banknote Authentication using Machine Learning

A Machine Learning project that predicts whether a banknote is **Genuine** or **Forged** using various classification algorithms. The project also includes a **Streamlit web application** for real-time predictions.

---
## 🚀 Live Demo
deployed Streamlit application:

🔗 **Streamlit App:**  https://banknote-autintication.streamlit.app/

## 📌 Project Overview

Counterfeit currency detection is an important problem in the banking and finance sector. This project uses the **Banknote Authentication Dataset** and compares multiple Machine Learning classification algorithms to determine whether a banknote is genuine or forged.

---

## 🎯 Problem Statement

Predict whether a banknote is:

- ✅ Genuine (Real)
- ❌ Forged (Fake)

using image-derived statistical features.

---

## 📂 Dataset

**Dataset:** Banknote Authentication Dataset

- Records: **1,372**
- Features: **4**
- Target: **Class**
- Missing Values: **No**

## Easy Example 📷

Imagine a photo:
- Variance	Difference in image colors and brightness.
- Skewness	Balance of the image pattern.
- Kurtosis	Sharpness of image details.
- Entropy	Complexity or randomness of the image.

## Note: In the Banknote Authentication dataset, these values are not entered manually. They are automatically extracted from a scanned image of the banknote. The machine learning model uses these four measurements to decide whether the banknote is Genuine or Forged. This is the simplest explanation to include in a college project or viva.

### Target

| Class | Meaning |
|-------|---------|
| 0 | Genuine |
| 1 | Forged |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## 🤖 Machine Learning Algorithms

The following classification algorithms were implemented:

- Logistic Regression
- Decision Tree
- Support Vector Machine (SVM)
- K-Nearest Neighbors (KNN)
- Naive Bayes

---

## 📊 Model Performance

| Algorithm | Accuracy |
|-----------|----------|
| Logistic Regression | 97.82% |
| Decision Tree | 98.18% |
| Support Vector Machine (SVM) | 100.00% |
| K-Nearest Neighbors (KNN) | 100.00% |
| Naive Bayes | 80.73% |

---

## 📁 Project Structure

```
Banknote-Authentication/
│
├── app.py
├── train_model.py
├── best_model.pkl
├── scaler.pkl          # Optional
├── BankNote_Authentication.csv
├── requirements.txt
├── README.md
└── images/
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/Banknote-Authentication.git
```

### Move into project folder

```bash
cd Banknote-Authentication
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Streamlit App

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📸 Web Application

The Streamlit application allows users to:

- Enter the four input features
- Click **Predict**
- View whether the banknote is Genuine or Forged

---

## 📈 Evaluation Metrics

The following metrics were used:

- Accuracy Score
- Confusion Matrix
- Classification Report
  - Precision
  - Recall
  - F1-Score

---

## 💾 Model Saving

The trained model is saved using Joblib.

```python
import joblib

joblib.dump(model, "best_model.pkl")
```

Load the model:

```python
model = joblib.load("best_model.pkl")
```

---

## 📦 Requirements

```
streamlit
scikit-learn
pandas
numpy
joblib
matplotlib
seaborn
```

---

## 📄 License

This project is created for educational purposes.

---

## 👨‍💻 Author

**Your Name**

GitHub: https://github.com/yourusername
