from fastapi import APIRouter, HTTPException


from app.api.deps import ComputingServiceDeps

router = APIRouter(prefix="/calculator", tags=["CALCULATOR"])


@router.get("/add")
def add(a: float, b: float, service: ComputingServiceDeps):
    return {"result": service.add(a, b)}


@router.get("/subtract")
def subtract(a: float, b: float, service: ComputingServiceDeps):
    return {"result": service.subtract(a, b)}


@router.get("/multiply")
def multiply(a: float, b: float, service: ComputingServiceDeps):
    return {"result": service.multiply(a, b)}


@router.get("/divide")
def divide(a: float, b: float, service: ComputingServiceDeps):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": service.divide(a, b)}


@router.get("/modulo")
def modulo(a: int, b: int, service: ComputingServiceDeps):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": service.modulo(a, b)}


@router.get("/integer-divide")
def integer_divide(a: int, b: int, service: ComputingServiceDeps):
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": service.integer_divide(a, b)}