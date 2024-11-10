# study_hours_app.py

import streamlit as st
import pandas as pd
from app.analysis import calculate_mean, calculate_confidence_interval
from app.visualizations import plot_study_hours

# Page title
st.title("Daily Study Hours Analysis App")
st.write("Upload a CSV file to analyze students' daily study hours.")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Load and display the data
    data = pd.read_csv(uploaded_file)
    
    if 'study_hours' not in data.columns:
        st.error("The uploaded CSV must contain a 'study_hours' column.")
    else:
        # Display data preview
        st.write("### Data Preview")
        st.dataframe(data.head())

        # Calculate statistics
        study_hours = data['study_hours']
        mean_study_hours = calculate_mean(study_hours)
        confidence_interval = calculate_confidence_interval(study_hours)

        # Display mean and confidence interval
        st.write(f"**Mean Study Hours**: {mean_study_hours:.2f} hours")
        st.write(f"**90% Confidence Interval**: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f}) hours")

        # Plot data
        st.write("### Visualization of Study Hours")
        fig = plot_study_hours(study_hours, mean_study_hours, confidence_interval)
        st.pyplot(fig)
