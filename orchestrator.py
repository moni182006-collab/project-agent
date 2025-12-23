from anomaly_detection import detect_anomalies
from data_qa_agent import data_qa_check
from rca_agent import root_cause_analysis
from business_agent import business_impact
from action_agent import recommended_actions


def run_orchestrator():
    df, anomalies = detect_anomalies()
    baseline = df[df["anomaly"] == 1]

    for _, row in anomalies.iterrows():
        qa_result = data_qa_check(row)
        if qa_result["status"] == "FAIL":
            continue

        rca = root_cause_analysis(row, baseline)
        business = business_impact(row)

        # Numeric-based action decision (robust)
        actions = recommended_actions(row, baseline)

        return {
            "timestamp": row["timestamp"],
            "llm_root_cause": rca["llm_root_cause"],
            "confidence": rca["confidence"],
            "business_impact": business,
            "actions": actions
        }
