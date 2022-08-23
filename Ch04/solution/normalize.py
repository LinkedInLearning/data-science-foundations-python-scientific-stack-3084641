import numpy as np

def by_zscore(values, dist=3):
    """Set every data point more than "dist" standard deviations to mean"""
    values = values.copy()
    z_score = (values - values.mean()) / values.std()
    mask = np.abs(z_score) > dist
    values[mask] = values.mean()
    return values