from typing import Annotated
from fastapi import Depends
from app.services.computing_service import ComputingService


def get_computing_service() -> ComputingService:
    return ComputingService(decimal_places=2)

ComputingServiceDeps = Annotated[ComputingService, Depends(get_computing_service)]