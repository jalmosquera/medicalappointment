from fastapi import FastAPI
from core.patiends.routes import router as patiendsRouter

app = FastAPI()

app.include_router(patiendsRouter)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
