from fastapi import APIRouter

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)