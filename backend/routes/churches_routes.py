from traceback import format_exc

from controllers.churches_control import ChurchesControl
from fastapi import APIRouter, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from helpers.errors import ErrorHandler
from schemas.churches_schema import Church

api_churches = APIRouter(prefix="/churches")


# Create a church
@api_churches.post(
    "/create/",
    description="Create a new church",
    tags=["churches"],
    status_code=200,
    response_description="Church created",
)
async def create_church(
    request: Request, data: Church, current_user: str
) -> JSONResponse:
    try:
        controller = ChurchesControl()
        results = controller.create_church(data=data, current_user=current_user)
        response: dict = {"results": results, "detail": "Church created!"}
        response_json = jsonable_encoder(response)
    except Exception as e:
        print(e)
        ErrorHandler.handle_error(
            route=request.url, exception=e, traceback=format_exc()
        )
    return JSONResponse(
        content=response_json, status_code=200, media_type="application/json"
    )


# Fetch churches
@api_churches.get(
    "/all/",
    description="Get all churches",
    tags=["churches"],
    status_code=200,
    response_description="Displaying churches",
)
async def get_all_churches(request: Request, current_user: str) -> JSONResponse:
    try:
        controller = ChurchesControl()
        results = controller.get_all_churches()
        response: dict = {"results": results, "detail": "Displaying Churches"}
        response_json = jsonable_encoder(response)
    except Exception as e:
        print(e)
        ErrorHandler.handle_error(
            route=request.url, exception=e, traceback=format_exc()
        )
    return JSONResponse(
        content=response_json, status_code=200, media_type="application/json"
    )
