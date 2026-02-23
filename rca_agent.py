def root_cause_analysis(row, baseline):
    # Relative deviations
    impacts = {
        "traffic": abs(row["traffic"] - baseline["traffic"].mean()) / baseline["traffic"].mean(),
        "revenue": abs(row["revenue"] - baseline["revenue"].mean()) / baseline["revenue"].mean(),
        "orders": abs(row["orders"] - baseline["orders"].mean()) / baseline["orders"].mean(),
        "conversion": abs(row["conversion_rate"] - baseline["conversion_rate"].mean()) / baseline["conversion_rate"].mean()
    }

    # Determine dominant factor (but do NOT force)
    dominant = max(impacts, key=impacts.get)
    dominant_score = impacts[dominant]

    # Severity tiers (EXPLANATORY, not filtering)
    if dominant_score < 0.2:
        severity = "Minor"
    elif dominant_score < 0.5:
        severity = "Moderate"
    else:
        severity = "Severe"

    # Root cause label
    if dominant_score < 0.15:
        root_cause = "Minor / Mixed Anomaly"
    else:
        root_cause = f"{dominant.capitalize()} Change"

    explanation = (
        f"Root Cause: {root_cause}\n\n"
        f"Severity: {severity}\n\n"
        f"Metric Impacts:\n"
        f"- Traffic Impact: {impacts['traffic']:.2f}\n"
        f"- Revenue Impact: {impacts['revenue']:.2f}\n"
        f"- Orders Impact: {impacts['orders']:.2f}\n"
        f"- Conversion Impact: {impacts['conversion']:.2f}\n\n"
        f"Explanation: The anomaly is driven by relative deviations across multiple metrics. "
        f"The dominant contributing factor is {dominant}, but other metrics also show measurable variation."
    )

    return {
        "llm_root_cause": explanation,
        "root_cause_label": root_cause,
        "severity": severity,
        "impacts": impacts
    }
