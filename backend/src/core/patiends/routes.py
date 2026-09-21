from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/patients")
def get_patiends(limit: int = Query(default=10, le=25, ge=1)) -> dict:
    return {"patiends": [], "limit": limit}
