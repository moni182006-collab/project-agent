def recommended_actions(anomaly_row, baseline_df):
    actions = []

    if anomaly_row["traffic"] < baseline_df["traffic"].mean() * 0.7:
        actions.append("Check marketing campaigns")
        actions.append("Verify app / website availability")

    if anomaly_row["conversion_rate"] < baseline_df["conversion_rate"].mean() * 0.9:
        actions.append("Review checkout funnel")
        actions.append("Investigate UX issues")

    return actions
