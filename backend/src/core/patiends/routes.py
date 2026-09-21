from fastapi import APIRouter

router = APIRouter()


@router.get("/patients")
def get_patiends() -> dict:
    return {"patiends": []}


@router.get("/patients/{patient_id}")
def get_partiend(patient_id: int) -> dict:
    return {"patient_id": id}
