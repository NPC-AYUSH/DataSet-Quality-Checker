import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_anomalies(df: pd.DataFrame) -> dict:
    # Use only numeric columns
    numeric_df = df.select_dtypes(include=["int64", "float64"])

    if numeric_df.empty:
        return {
            "anomaly_ratio": 0.0,
            "anomaly_count": 0,
            "message": "No numeric columns available for anomaly detection"
        }

    model = IsolationForest(
        n_estimators=100,
        contamination=0.05,
        random_state=42
    )

    predictions = model.fit_predict(numeric_df)

    # -1 = anomaly, 1 = normal
    anomaly_count = int((predictions == -1).sum())
    anomaly_ratio = round(anomaly_count / len(df), 4)

    return {
        "anomaly_count": anomaly_count,
        "anomaly_ratio": anomaly_ratio
    }
