# app/visualizations.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_study_hours(data: pd.Series, sample_mean: float, confidence_interval: tuple):
    """Create a scatter plot of study hours with mean and confidence interval."""
    n = len(data)
    fig, ax = plt.subplots()
    ax.scatter(range(1, n + 1), data, color='blue', label='Daily Study Hours')
    ax.axhline(y=sample_mean, color='orange', linestyle='-', label='Sample Mean')
    ax.fill_between(range(1, n + 1), confidence_interval[0], confidence_interval[1], color='lightgrey', alpha=0.4, label='90% Confidence Interval')
    ax.set_title("Daily Study Hours of Students")
    ax.set_xlabel("Student Number")
    ax.set_ylabel("Daily Study Hours")
    ax.legend()
    return fig
