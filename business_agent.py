def business_impact(row):
    return {
        "impact_level": "HIGH",
        "summary": f"""
Revenue dropped to ₹{row['revenue']}.
Traffic declined sharply while conversion remained healthy.
This indicates top-of-funnel acquisition failure.
Estimated short-term loss is significant if unresolved.
"""
    }
