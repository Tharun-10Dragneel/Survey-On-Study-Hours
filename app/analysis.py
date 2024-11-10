# app/analysis.py
import numpy as np
from scipy import stats
import pandas as pd

def calculate_mean(data: pd.Series) -> float:
    """Calculate the mean of the study hours."""
    return data.mean()

def calculate_confidence_interval(data: pd.Series, confidence_level: float = 0.90):
    """Calculate a confidence interval for the study hours using the t-distribution."""
    sample_mean = data.mean()
    sample_std = data.std(ddof=1)
    n = len(data)
    return stats.t.interval(confidence_level, df=n-1, loc=sample_mean, scale=sample_std/np.sqrt(n))
