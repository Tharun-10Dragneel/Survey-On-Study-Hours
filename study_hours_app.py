import streamlit as st
import pandas as pd
from app.analysis import calculate_mean, calculate_confidence_interval
from app.visualizations import plot_study_hours

# Page title and header
st.set_page_config(page_title="Study Hours Analysis", page_icon="📊", layout="centered")

# Custom CSS for dark theme with white text
st.markdown("""
    <style>
    .main {
        background-color: #333;
        color: white;
    }
    h1, h2, h3, p {
        color: white;
        text-align: center;
    }
    .header {
        background-color: #1c1c1c;
        color: white;
        padding: 1rem;
        border-radius: 10px;
        font-size: 1.5rem;
        text-align: center;
    }
    .upload-section, .results-section {
        background-color: #444;
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        box-shadow: 0px 0px 10px rgba(255, 255, 255, 0.1);
    }
    .upload-section {
        background-color: #222;
    }
    .btn {
        display: flex;
        justify-content: center;
    }
    .footer {
        text-align: center;
        color: #bbb;
        font-size: 0.9rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>📊 Study Hours Analysis App 📊</div>", unsafe_allow_html=True)

# Introduction
st.write("Welcome to the **Study Hours Analysis App**! Upload a CSV file containing students' daily study hours data, and this app will provide insights, including the mean study hours and the 90% confidence interval. It will also visualize the study hours for a better understanding of the data.")

# File uploader section
st.markdown("<div class='upload-section'>", unsafe_allow_html=True)
st.subheader("Upload Your Data")
st.write("Upload a CSV file that contains a column named `study_hours` to analyze the data.")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    # Load and display the data
    data = pd.read_csv(uploaded_file)
    
    # Check if the required 'study_hours' column exists
    if 'study_hours' not in data.columns:
        st.error("The uploaded CSV must contain a 'study_hours' column.")
    else:
        # Display data preview
        st.write("### Data Preview")
        st.dataframe(data.head())

        # Calculate and display the mean and confidence interval
        study_hours = data['study_hours']
        mean_study_hours = calculate_mean(study_hours)
        confidence_interval = calculate_confidence_interval(study_hours)

        st.write(f"### **Mean Study Hours**: {mean_study_hours:.2f} hours")
        st.write(f"### **90% Confidence Interval**: ({confidence_interval[0]:.2f}, {confidence_interval[1]:.2f}) hours")

        # Plot visualization
        st.write("### Visualization of Study Hours")
        fig = plot_study_hours(study_hours, mean_study_hours, confidence_interval)
        st.pyplot(fig)

        # Hypothetical 2 hours study time
        hypothetical_value = 2
        st.write(f"### Comparison with Recommended Study Time: {hypothetical_value} hours")

        if mean_study_hours < hypothetical_value:
            st.write(f"The mean study time ({mean_study_hours:.2f} hours) is less than the recommended {hypothetical_value} hours of study per day.")
        elif mean_study_hours > hypothetical_value:
            st.write(f"The mean study time ({mean_study_hours:.2f} hours) is more than the recommended {hypothetical_value} hours of study per day.")
        else:
            st.write(f"The mean study time is exactly equal to the recommended {hypothetical_value} hours.")

        # Reflection
        st.write("### Reflection on Study Patterns")
        st.write("Consider how your data compares to the recommended study time. Does it indicate that most students are under-studying or over-studying compared to the recommendation?")

    # End of file upload section
    st.markdown("</div>", unsafe_allow_html=True)

# Footer section
st.markdown("<div class='footer'>Made with ❤️ using Streamlit</div>", unsafe_allow_html=True)
