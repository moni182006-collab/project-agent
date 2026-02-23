def data_qa_check(anomaly_row):
    issues = []

    for col in ["orders", "revenue", "traffic", "conversion_rate"]:
        if anomaly_row[col] is None:
            issues.append(f"Missing value in {col}")
        if anomaly_row[col] == 0:
            issues.append(f"Zero value in {col}")

    if issues:
        return {
            "status": "FAIL",
            "issues": issues
        }

    return {
        "status": "PASS",
        "issues": []
    }
