import streamlit as st
import joblib
import numpy as np

# Load the saved SVM model
model = joblib.load("svm_model.pkl")

# Streamlit app title
st.title("🔮 SVM Predictor")

# Input section for features
st.header("Enter feature values:")

# Example: 10 features (you can adjust based on your dataset)
mean_radius = st.number_input("mean radius:", value=0.0)
mean_perimeter = st.number_input("mean perimeter", value=0.0)
mean_area = st.number_input("mean area':", value=0.0)
mean_concavity = st.number_input("mean concavity:", value=0.0)
mean_concave_points1 = st.number_input("mean concave points:", value=0.0)
worst_radius = st.number_input("worst radius:", value=0.0)
worst_perimeter = st.number_input("worst perimeter:", value=0.0)
worst_area = st.number_input("worst area:", value=0.0)
worst_concavity1 = st.number_input("worst concavity:", value=0.0)
worst_concave_points1 = st.number_input("worst concave points:", value=0.0)
# Button to make prediction
if st.button("Predict"):
    # Prepare input as 2D array (sklearn requires this format)
    input_data = np.array([[mean_radius, mean_perimeter, mean_area, mean_concavity, mean_concave_points1, worst_radius, worst_perimeter, worst_area, worst_concavity1, worst_concave_points1]])

    # Make prediction using the loaded model
    prediction = model.predict(input_data)
    
    # Show result
    result = "Yes" if prediction[0] == 1 else "No"
    st.success(f"✅ Predicted class: {result}")