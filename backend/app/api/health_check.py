from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["HEALTH"])

@router.get("")
def do_health_check():
    return "OK"