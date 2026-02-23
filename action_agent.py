def recommended_actions(row, baseline):
    actions = []

    if row["traffic"] < baseline["traffic"].mean() * 0.7:
        actions.append("Check marketing campaigns")
        actions.append("Verify app / website availability")

    if row["conversion_rate"] < baseline["conversion_rate"].mean() * 0.9:
        actions.append("Review checkout funnel")

    return actions
