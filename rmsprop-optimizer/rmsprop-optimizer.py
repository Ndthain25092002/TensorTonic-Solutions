import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    w = np.array(w)  # Ensure w is a numpy array
    g = np.array(g)  # Ensure g is a numpy array
    s = np.array(s)  # Ensure s is a numpy array
    s_new = np.array(s)  # Ensure s is a numpy array\
    w_new = np.array(w)  # Ensure w is a numpy array

    s_new = beta * s + (1 - beta) * g**2
    w_new = w - lr * g / (np.sqrt(s_new) + eps)

    return w_new, s_new

