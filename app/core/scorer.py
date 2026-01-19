def compute_quality_score(
    missing_ratio: float,
    duplicate_ratio: float,
    anomaly_ratio: float | None
) -> dict:
    score = 100

    score -= missing_ratio * 40
    score -= duplicate_ratio * 30

    if anomaly_ratio is not None:
        score -= anomaly_ratio * 30

    score = round(max(0, min(100, score)), 2)

    if score >= 85:
        verdict = "Excellent"
    elif score >= 70:
        verdict = "Good"
    elif score >= 50:
        verdict = "Fair"
    else:
        verdict = "Poor"

    return {
        "score": score,
        "verdict": verdict
    }
