def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """

    ranked_items = []

    for item in list(items):
        votes = item[1]
        rating = item[0]

        weighted_rating = (votes / (votes + min_votes)) * rating + (min_votes / (votes + min_votes)) * global_mean
        ranked_items.append(weighted_rating)  # item[2] is the item identifier

    return ranked_items