import streamlit as st
import plotly.graph_objects as go
from orchestrator import run_orchestrator
from evaluation import evaluate_system

st.set_page_config("Agentic Data QA System", layout="wide")

st.title("📊 Agentic Data QA System")
st.caption("Autonomous Anomaly Detection & Root Cause Analysis")

# ---------------- STATE INIT ----------------
if "reports" not in st.session_state:
    st.session_state.reports = None
    st.session_state.df = None
    st.session_state.exec_time = None

# ---------------- RUN PIPELINE ----------------
if st.button("🚨 Run Investigation"):
    with st.spinner("Running full pipeline..."):
        df, reports, exec_time = run_orchestrator()

    st.session_state.df = df
    st.session_state.reports = reports
    st.session_state.exec_time = exec_time

    st.success("Incident analysis completed")

# ---------------- STOP IF NOT RUN ----------------
if st.session_state.reports is None:
    st.info("Click **Run Investigation** to begin.")
    st.stop()

df = st.session_state.df
reports = st.session_state.reports
exec_time = st.session_state.exec_time

# ---------------- GRAPH ----------------
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df["timestamp"],
    y=df["revenue"],
    mode="lines",
    name="Revenue"
))

fig.add_trace(go.Scatter(
    x=df[df["anomaly"] == -1]["timestamp"],
    y=df[df["anomaly"] == -1]["revenue"],
    mode="markers",
    name="Anomaly",
    marker=dict(color="red", size=10)
))

fig.update_layout(
    title="Revenue Time Series with Anomalies",
    xaxis_title="Date",
    yaxis_title="Revenue"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- DROPDOWN (FIXED) ----------------
st.subheader("Select Anomaly")

labels = {
    f"Anomaly {i+1} - {r['timestamp']}": r
    for i, r in enumerate(reports)
}

selected_label = st.selectbox("Anomalies", list(labels.keys()))
report = labels[selected_label]   # ✅ THIS NOW WORKS

# ---------------- REPORT ----------------
st.markdown("### 🧠 Root Cause (Structured LLM)")
st.markdown(report["llm_root_cause"])

st.markdown("### 💼 Business Impact")
st.write(report["business_impact"]["summary"])

st.markdown("### 🛠 Recommended Actions")
for a in report["actions"]:
    st.write(f"- {a}")

st.markdown(f"🔐 **Trust Score:** {report['trust_score']}/100")

# ---------------- EVALUATION (LAST) ----------------
explained = sum(1 for r in reports if r["llm_root_cause"])
eval_metrics = evaluate_system(exec_time, len(reports), explained)

st.markdown("### 📈 Evaluation Metrics")
st.write(f"✅ Anomalies Explained: {eval_metrics['anomalies_explained']}")
st.write(f"⏱ Time Taken (seconds): {eval_metrics['time_taken_seconds']}")
st.write(f"🕒 Estimated Manual Time (minutes): {eval_metrics['estimated_manual_time_minutes']}")
st.write(f"🚀 Time Reduction (%): {eval_metrics['time_reduction_percent']}")
