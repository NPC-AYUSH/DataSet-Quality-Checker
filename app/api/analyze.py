from fastapi import APIRouter, UploadFile, File, HTTPException
from app.core.loader import load_csv
from app.core.profiler import profile_dataset
from app.core.quality import compute_basic_quality
from app.schemas.response import AnalysisResponse
from app.core.anomaly import detect_anomalies
from app.core.scorer import compute_quality_score   
from app.core.suggestions import generate_suggestions
from app.core.cleaner import clean_dataset
from app.utils.storage import save_dataset



router = APIRouter(prefix="/analyze", tags=["Analysis"])

@router.post("/", response_model=AnalysisResponse)
async def analyze_dataset(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files supported")

    df = load_csv(file)

    profile = profile_dataset(df)
    quality = compute_basic_quality(df)
    anomalies = detect_anomalies(df)

    anomaly_ratio = anomalies.get("anomaly_ratio")

    quality_score = compute_quality_score(
        missing_ratio=quality["missing_ratio"],
        duplicate_ratio=quality["duplicate_ratio"],
        anomaly_ratio=anomaly_ratio
    )

    suggestions = generate_suggestions(
        df=df,
        missing_percentage=profile["missing_percentage"],
        duplicate_ratio=quality["duplicate_ratio"],
        anomaly_ratio=anomaly_ratio
    )
    cleaned_df = clean_dataset(df)
    dataset_id = save_dataset(cleaned_df)

    return {
        "filename": file.filename,
        "profile": profile,
        "quality": quality,
        "anomalies": anomalies,
        "quality_score": quality_score,
        "suggestions": {"recommendations": suggestions},
        "dataset_id": dataset_id
    }
