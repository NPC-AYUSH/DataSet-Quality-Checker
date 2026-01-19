import pandas as pd
from fastapi import UploadFile, HTTPException

def load_csv(file: UploadFile) -> pd.DataFrame:
    try:
        df = pd.read_csv(file.file)
        if df.empty:
            raise HTTPException(status_code=400, detail="Uploaded CSV is empty")
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid CSV file: {str(e)}")
