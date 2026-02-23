def compute_confidence(row, baseline, impacts):
    """
    Confidence is based on:
    - Strength of dominant signal
    - Distribution gap between dominant and others
    """

    sorted_impacts = sorted(impacts.values(), reverse=True)

    if max(sorted_impacts) == 0:
        return 0.0

    dominance_gap = sorted_impacts[0] - (sum(sorted_impacts[1:]) / 3)

    confidence = (0.6 * sorted_impacts[0]) + (0.4 * dominance_gap)

    return round(min(confidence * 100, 100), 2)
