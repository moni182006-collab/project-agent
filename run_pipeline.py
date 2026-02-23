from orchestrator import run_orchestrator

def main():
    df, reports, exec_time = run_orchestrator()

    print("\n==============================")
    print("AGENTIC DATA QA REPORT")
    print("==============================")

    for i, r in enumerate(reports, 1):
        print(f"\n===== ANOMALY {i} =====")
        print("Timestamp:", r["timestamp"])
        print("\nRoot Cause Analysis:")
        print(r["llm_root_cause"])
        print("\nBusiness Impact:")
        print(r["business_impact"]["summary"])
        print("\nRecommended Actions:")
        for a in r["actions"]:
            print("-", a)
        print("\nTrust Score:", r["trust_score"])

    print("\nExecution Time:", exec_time, "seconds")


if __name__ == "__main__":
    main()