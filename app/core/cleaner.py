import pandas as pd
from sklearn.ensemble import IsolationForest

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates
    cleaned_df = df.drop_duplicates()

    # Remove anomalies (numeric only)
    numeric_df = cleaned_df.select_dtypes(include=["int64", "float64"])

    if not numeric_df.empty:
        model = IsolationForest(
            contamination=0.05,
            random_state=42
        )
        preds = model.fit_predict(numeric_df)

        # Keep only normal rows
        cleaned_df = cleaned_df[preds == 1]

    return cleaned_df
