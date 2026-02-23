import pandas as pd
import warnings
from sklearn.ensemble import IsolationForest

# Silence pandas chained-assignment FutureWarning
warnings.filterwarnings("ignore", category=FutureWarning)

def detect_anomalies():
    # Load processed sales data
    df = pd.read_csv("data/sales.csv")

    # Ensure timestamp column is datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Features for anomaly detection
    features = df[["orders", "revenue", "traffic", "conversion_rate"]]

    # Isolation Forest model
    model = IsolationForest(contamination=0.25, random_state=42)

    # Fit and predict
    df["anomaly"] = model.fit_predict(features)

    # Extract anomalies
    anomalies = df[df["anomaly"] == -1].copy()

    return df, anomalies