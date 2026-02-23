import time
from anomaly_detection import detect_anomalies
from rca_agent import root_cause_analysis
from business_agent import business_impact
from action_agent import recommended_actions
from confidence import compute_confidence


def run_orchestrator():
    start = time.time()

    df, anomalies = detect_anomalies()
    baseline = df[df["anomaly"] == 1]

    reports = []

    for _, row in anomalies.iterrows():
        rca = root_cause_analysis(row, baseline)

        trust_score = compute_confidence(
            row,
            baseline,
            rca["impacts"]
        )

        reports.append({
            "timestamp": row["timestamp"],
            "llm_root_cause": rca["llm_root_cause"],
            "root_cause_label": rca["root_cause_label"],
            "severity": rca["severity"],
            "impacts": rca["impacts"],
            "trust_score": trust_score,
            "business_impact": business_impact(row),
            "actions": recommended_actions(row, baseline)
        })

    exec_time = round(time.time() - start, 2)

    return df, reports, exec_time
