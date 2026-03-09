import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    Given class labels from a decision tree node, compute the entropy using the stable logarithm formula.

Entropy is a fundamental concept from information theory that measures the amount of uncertainty or randomness in a dataset. In decision trees, it's used as a splitting criterion to build trees that maximize information gain.
    """
    # Use np.unique() with return_counts=True to get class frequencies.
    # Calculate probabilities by dividing class counts by the total number of samples.

    y = np.array(y)
    if len(y) == 0: 
        return 0.0  # Return zero entropy for empty nodes   
    class_counts = np.bincount(y)
    probabilities = class_counts / len(y)   
    # Filter out zero probabilities before computing logarithms to avoid numerical issues.

    non_zero_probs = probabilities[probabilities > 0]
    entropy = -np.sum(non_zero_probs * np.log2(non_zero_probs))
    # Note: We use np.log2() for base-2 logarithms, which is standard for entropy calculations in decision trees.
    # Use np.log2() for base-2 logarithms in the entropy
    
    return entropy