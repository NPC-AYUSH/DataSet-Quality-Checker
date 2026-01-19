from pydantic import BaseModel
from typing import Dict, Any,List

class DatasetProfile(BaseModel):
    rows: int
    columns: int
    data_types: Dict[str, str]
    missing_values: Dict[str, int]
    missing_percentage: Dict[str, float]
    duplicate_rows: int

class QualityMetrics(BaseModel):
    total_cells: int
    missing_cells: int
    missing_ratio: float
    duplicate_ratio: float

class AnomalyReport(BaseModel):
    anomaly_count: int
    anomaly_ratio: float | None = None
    message: str | None = None

class QualityScore(BaseModel):
    score: float
    verdict: str

class Suggestions(BaseModel):
    recommendations: List[str]

class AnalysisResponse(BaseModel):
    filename: str
    profile: DatasetProfile
    quality: QualityMetrics
    anomalies: AnomalyReport
    quality_score: QualityScore
    suggestions: Suggestions





