import pandas as pd

def compute_basic_quality(df: pd.DataFrame) -> dict:
    total_cells = df.shape[0] * df.shape[1]
    missing_cells = int(df.isnull().sum().sum())
    duplicate_ratio = df.duplicated().mean()

    return {
        "total_cells": total_cells,
        "missing_cells": missing_cells,
        "missing_ratio": round(missing_cells / total_cells, 4),
        "duplicate_ratio": round(duplicate_ratio, 4)
    }
