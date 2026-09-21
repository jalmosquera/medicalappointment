from fastapi import APIRouter

router = APIRouter()


@router.get("/patients")
def get_patiends(limit: int = 10) -> dict:
    return {"patiends": [], "limit": limit}
