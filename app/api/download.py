from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.utils.storage import get_dataset
import io

router = APIRouter(prefix="/download", tags=["Download"])

@router.get("/{dataset_id}")
def download_cleaned_dataset(dataset_id: str):
    df = get_dataset(dataset_id)
    if df is None:
        raise HTTPException(status_code=404, detail="Dataset not found")

    stream = io.StringIO()
    df.to_csv(stream, index=False)
    stream.seek(0)

    return StreamingResponse(
        stream,
        media_type="text/csv",
        headers={
            "Content-Disposition": f"attachment; filename=cleaned_dataset.csv"
        }
    )
