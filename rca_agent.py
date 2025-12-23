import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def root_cause_analysis(anomaly_row, baseline_df):

    prompt = f"""
You are a senior data analyst.

Anomalous metrics:
Orders: {anomaly_row['orders']}
Revenue: {anomaly_row['revenue']}
Traffic: {anomaly_row['traffic']}
Conversion Rate: {anomaly_row['conversion_rate']}

Historical averages:
Orders: {baseline_df['orders'].mean()}
Revenue: {baseline_df['revenue'].mean()}
Traffic: {baseline_df['traffic'].mean()}
Conversion Rate: {baseline_df['conversion_rate'].mean()}

Tasks:
1. Identify the most likely root cause.
   - If traffic has dropped significantly (more than 30%), prioritize acquisition issues,
     even if conversion rate has increased.
2. Use numeric comparison to justify why other causes are less likely.
3. Provide a concise business-friendly explanation (5–6 sentences).
"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return {
        "llm_root_cause": response.choices[0].message.content,
        "confidence": "Cloud LLM (Groq LLaMA-3.1-8B)"
    }
