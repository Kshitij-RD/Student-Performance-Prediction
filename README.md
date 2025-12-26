# Student Performance Prediction

An end-to-end Machine Learning project designed to predict student academic performance (specifically math scores) based on various demographic and academic factors. The project includes a complete pipeline from data ingestion to deployment using a Flask web application.

## 📌 Project Overview

This application utilizes a machine learning model to estimate a student's potential score based on inputs such as:
* **Demographics:** Gender, Race/Ethnicity, Parental Level of Education.
* **Socio-economic:** Lunch type.
* **Academic History:** Test preparation course completion.
* **Current Metrics:** Reading Score, Writing Score.

The system is architected with modular components for scalability and maintainability, following industry best practices.

## 🛠️ Tech Stack

* **Programming Language:** Python 3.8+
* **Web Framework:** Flask
* **Machine Learning:** Scikit-Learn, XGBoost
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Deployment:** Docker (optional/ready for containerization)

## 📂 Project Structure

```text
├── artifacts/              # Stores generated files (models, preprocessors, datasets)
├── notebook/               # Jupyter notebooks for EDA and Model Prototyping
├── src/                    # Source code for the project
│   ├── components/         # Core ML components (Ingestion, Transformation, Training)
│   ├── pipeline/           # Prediction and Training pipelines
│   ├── utils.py            # Utility functions (save/load objects)
│   ├── logger.py           # Custom logging setup
│   └── exception.py        # Custom exception handling
├── templates/              # HTML templates for the Flask app
├── app.py                  # Entry point for the Flask application
├── requirements.txt        # List of dependencies
├── setup.py                # Package installer script
└── README.md               # Project documentation

🧠 Machine Learning Pipeline

The project implements a modular pipeline located in the src/ directory:

Data Ingestion (src/components/data_ingestion.py):

Reads the raw data from the source (CSV).

Splits the dataset into Training and Testing sets.

Saves the artifacts to the artifacts/ folder.

Data Transformation (src/components/data_transformation.py):

Handles missing values and data cleaning.

Performs One-Hot Encoding for categorical variables.

Standardizes numerical features.

Saves the preprocessor.pkl object.

Model Trainer (src/components/model_trainer.py):

Trains multiple regression models (Random Forest, Decision Tree, XGBoost, etc.).

Evaluates models based on R2 Score.

Selects the best performing model and saves it as model.pkl.

Prediction Pipeline (src/pipeline/predict_pipeline.py):

Loads the saved model.pkl and preprocessor.pkl.

Transforms user input data from the web form.

Returns the prediction to the Flask app.

📊 Exploratory Data Analysis (EDA)


Detailed analysis of the dataset is available in the notebook/ directory, covering:

Distribution of scores across different demographics.

Correlation analysis between features.

Impact of test preparation courses on final results.
