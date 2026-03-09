import numpy as np

def percentiles(x, q):
    """
    Compute percentiles using linear interpolation.
    Compute percentiles of a dataset using linear interpolation.

    Function Arguments
    x: list or array - Numeric data
    q: list or array - Percentile values (0-100)
    """
    # Write code here

    x = np.array(x)
    q = np.array(q)

    # Use np.percentile() with method='linear'.
    return np.percentile(x, q, method='linear')
