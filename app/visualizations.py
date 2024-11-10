import matplotlib.pyplot as plt
import numpy as np

def plot_study_hours(study_hours, mean, confidence_interval):
    # Create a scatter plot of study hours
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(np.arange(len(study_hours)), study_hours, color='skyblue', label='Study Hours', alpha=0.6)

    # Mark the sample mean with a red line
    ax.axhline(mean, color='red', linestyle='--', label=f'Mean: {mean:.2f} hours')

    # Shade the area between the confidence interval
    ax.fill_between(np.arange(len(study_hours)), confidence_interval[0], confidence_interval[1], color='orange', alpha=0.3, label=f'90% Confidence Interval')

    # Add labels and title
    ax.set_title("Study Hours Distribution with Mean and Confidence Interval", fontsize=16)
    ax.set_xlabel("Student Index", fontsize=14)
    ax.set_ylabel("Study Hours (hours)", fontsize=14)

    # Show legend
    ax.legend(loc='upper right')

    # Return the figure
    return fig
