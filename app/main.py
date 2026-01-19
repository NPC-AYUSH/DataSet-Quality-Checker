from fastapi import FastAPI
from app.api.analyze import router as analyze_router
from app.api.download import router as download_router

app = FastAPI(title="Dataset Quality Checker")

app.include_router(analyze_router)
app.include_router(download_router)

@app.get("/")
def health():
    return {"status": "ok"}
