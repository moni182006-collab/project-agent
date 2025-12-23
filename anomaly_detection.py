import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies():
    df = pd.read_csv("data/sales.csv")
    
    features = df[["orders", "revenue", "traffic", "conversion_rate"]]

    model = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = model.fit_predict(features)

    anomalies = df[df["anomaly"] == -1]
    return df, anomalies
