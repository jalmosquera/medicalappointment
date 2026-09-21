from fastapi import APIRouter, Query

from src.core.patiends.models import PatientCreate

router = APIRouter()


@router.post("/patients")
def create_patiends(patiends: PatientCreate) -> dict:
    data = {"name": patiends.name, "email": patiends.email, "age": patiends.age}
    return data


@router.get("/patients")
def get_patiends(limit: int = Query(default=10, le=25, ge=1)) -> dict:
    return {"patiends": [], "limit": limit}
