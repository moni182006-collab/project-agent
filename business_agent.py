def business_impact(row):
    return {
        "impact_level": "HIGH",
        "summary": (
            f"Revenue dropped to ₹{row['revenue']}. "
            f"Traffic declined sharply while conversion remained healthy. "
            f"This indicates top-of-funnel acquisition failure."
        )
    }
