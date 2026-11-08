from fastapi import APIRouter

from .health_check import router as health_router
from .calculator import router as calculator_router

router = APIRouter(prefix="/api/v1")
router.include_router(health_router)
router.include_router(calculator_router)