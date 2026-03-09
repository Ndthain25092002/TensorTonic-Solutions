def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    Precision@k and recall@k are the standard metrics for evaluating top-k recommendation lists. Precision@k measures what fraction of the recommended items are relevant, while recall@k measures what fraction of all relevant items were recommended. Together they capture the trade-off between recommendation quality and coverage.

    Given a ranked list of recommended items, a set of relevant (ground truth) items, and a cutoff k, compute both precision@k and recall@k.
    """

    recommended = list(recommended)  # Ensure it's a list
    relevant = set(relevant)  # Convert to set for O(1) lookups 

    # Get the top-k recommended items
    top_k_recommended = recommended[:k]

    relevant_and_recommended = set(top_k_recommended) & relevant
    precision = len(relevant_and_recommended) / k if k > 0 else 0
    recall = len(relevant_and_recommended) / len(relevant) if relevant else 0

    return [precision, recall]
