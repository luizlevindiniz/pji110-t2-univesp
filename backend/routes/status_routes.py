from typing import Literal

from fastapi import APIRouter, Request

api_status = APIRouter(prefix="/status")


# Check App Status
@api_status.get("/", description="Check app status", tags=["status"], status_code=200)
async def get_status(request: Request) -> dict:
    return {"msg": "Online"}
