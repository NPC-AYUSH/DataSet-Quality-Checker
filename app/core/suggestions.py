import pandas as pd

def generate_suggestions(
    df: pd.DataFrame,
    missing_percentage: dict,
    duplicate_ratio: float,
    anomaly_ratio: float | None
) -> list[str]:
    suggestions = []

    # Missing values suggestions
    for column, percent in missing_percentage.items():
        if percent > 20:
            suggestions.append(
                f"Column '{column}' has {percent}% missing values. "
                f"Consider dropping this column or applying advanced imputation."
            )
        elif percent > 5:
            suggestions.append(
                f"Column '{column}' has {percent}% missing values. "
                f"Consider mean/median or mode imputation."
            )

    # Duplicate rows suggestion
    if duplicate_ratio > 0.05:
        suggestions.append(
            "High number of duplicate rows detected. "
            "Consider removing duplicates to avoid biased analysis."
        )

    # Anomaly suggestion
    if anomaly_ratio is not None and anomaly_ratio > 0.05:
        suggestions.append(
            "Significant number of anomalous rows detected. "
            "Review outliers before training models or generating insights."
        )

    if not suggestions:
        suggestions.append("Dataset looks clean. No major quality issues detected.")

    return suggestions
