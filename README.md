Heart Disease Prediction – Real-World ML Pipeline Project
📌 Problem Definition

Heart disease is one of the leading causes of death worldwide. Early detection can save lives by enabling timely lifestyle changes and medical care.
This project builds a machine learning pipeline to predict whether a person is at risk of heart disease based on clinical and demographic features such as age, cholesterol, chest pain type, and blood pressure.

⚙️ ML Pipeline Steps
🔹 1. Data Preprocessing

Handled missing values (if any).

Encoded categorical variables (e.g., chest pain type, thal).

Scaled numerical features (e.g., age, cholesterol, resting blood pressure).

🔹 2. Feature Engineering

Created a new feature: chol_per_age = cholesterol / age, which gives cholesterol risk relative to age.

🔹 3. Model Selection

Used Logistic Regression as the main classification model (simple, interpretable, and effective).

Evaluated using accuracy score.

📊 Results

The model achieved good accuracy on the test set (printed in train.py).

Shows which features are most important for predicting risk.

🌍 Real-World Usefulness

Doctors or health workers can use such a system for initial screening of patients.

Helps in identifying high-risk patients early without expensive medical tests.

Supports public health initiatives by predicting heart disease trends in populations.

📂 Project Structure
ml_pipeline_project/
│── data/
│   └── heart.csv
│── models/          (optional, if saving models)
│── src/
│   ├── data_downloader.py   # downloads dataset
│   ├── check_data.py        # check dataset structure
│   ├── train.py             # trains pipeline + prints accuracy
│   └── pipeline.py          # sklearn pipeline setup
│── requirements.txt
│── README.md

🚀 How to Run

Download dataset:

python src/data_downloader.py


Check dataset:

python src/check_data.py


Train the model:

python src/train.py