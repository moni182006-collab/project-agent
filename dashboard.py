import streamlit as st
from orchestrator import run_orchestrator

st.set_page_config(
    page_title="Agentic Data QA Dashboard",
    layout="centered"
)

st.title("📊 Agentic Data QA System")
st.subheader("Autonomous Anomaly Detection & Root Cause Analysis")

st.markdown("---")

if st.button("🚨 Run Incident Analysis"):
    with st.spinner("Analyzing data and generating insights..."):
        report = run_orchestrator()

    st.success("Incident analysis completed")

    st.markdown("### 📅 Incident Timestamp")
    st.write(report["timestamp"])

    st.markdown("### 🧠 Root Cause (LLM Explanation)")
    st.markdown(report["llm_root_cause"])

    st.markdown("### 💼 Business Impact")
    st.write(report["business_impact"]["summary"])

    st.markdown("### 🛠 Recommended Actions")
    for action in report["actions"]:
        st.write(f"- {action}")
