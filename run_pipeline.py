from orchestrator import run_orchestrator

if __name__ == "__main__":
    report = run_orchestrator()
    print("\n📌 INCIDENT REPORT\n")
    for k, v in report.items():
        print(f"{k}: {v}")
