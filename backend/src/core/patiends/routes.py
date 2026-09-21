from fastapi import APIRouter

router = APIRouter()


@router.get("/patiends")
def get_patiends() -> dict:
    return {"patiends": []}

