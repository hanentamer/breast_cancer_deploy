# Breast Cancer Detection & Streamlit Deploymentt

This project uses machine learning to classify breast cancer as malignant or benign using the [Breast Cancer Wisconsin dataset](https://scikit-learn.org/stable/datasets/toy_dataset.html#breast-cancer-dataset) from scikit-learn. The trained model is deployed as a web app using [Streamlit](https://streamlit.io/).

## Features

- Data exploration and visualization
- Model training with Decision Tree, Random Forest, and SVM
- Hyperparameter tuning using GridSearchCV
- Model evaluation and comparison
- Deployment of the best model with Streamlit

## Project Structure

```
project-1.ipynb         # Jupyter notebook with data analysis and model training
streamlit_proj1.py      # Streamlit app for model deployment
svm_model.pkl           # Trained SVM model (pickle file)
requirements.txt        # Python dependencies
Readme.md               # Project documentation
```

## Getting Started

### 1. Clone the repository

```sh
git clone https://github.com/yourusername/breast_cancer_deploy.git
cd breast_cancer_deploy
```

### 2. Install dependencies

It is recommended to use a virtual environment.

```sh
pip install -r requirements.txt
```

### 3. Run the Streamlit app

```sh
streamlit run streamlit_proj1.py
```

## Usage

- Open the Streamlit app in your browser.
- Enter the required features to get a prediction (malignant or benign).

## Model Training

All steps for data preprocessing, model training, evaluation, and saving the model are documented in [project-1.ipynb](project-1.ipynb).

## License

This project is licensed under the MIT License.

## Acknowledgements

- [scikit-learn](https://scikit-learn.org/)
