import os
from typing import Any, Dict

import dotenv
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from routes.churches_routes import api_churches
from routes.status_routes import api_status
from starlette.middleware.sessions import SessionMiddleware

# Env
env_path = dotenv.find_dotenv(".env", raise_error_if_not_found=True)
dotenv.load_dotenv(dotenv_path=env_path)

COOKIE = os.getenv("PROJECT_COOKIE")
PROJECT_NAME = os.getenv("PROJECT_NAME")
PROJECT_TITLE = os.getenv("PROJECT_TITLE")
DESCRIPTION = os.getenv("PROJECT_DESCRIPTION")
GITHUB = os.getenv("PROJECT_GIT_URL")
VERSION = os.getenv("PROJECT_VERSION")


# Print on startup
print(PROJECT_NAME.upper() if isinstance(PROJECT_NAME, str) else "PROJETO")

# Initializing FastAPI
app = FastAPI()

# Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(
    SessionMiddleware,
    secret_key="123",
    session_cookie=COOKIE,
    https_only=False,
)

# API Router
api = APIRouter(prefix="/api")
# Routes
api.include_router(api_status)
api.include_router(api_churches)
# Appending api on app
app.include_router(api)


# Swagger Config
def custom_openapi() -> Dict[str, Any]:
    description: str = f'{DESCRIPTION} <br><br> <a href="{str(GITHUB)}">GitHub</a>'
    assert (
        isinstance(description, str)
        and isinstance(PROJECT_TITLE, str)
        and isinstance(VERSION, str)
    )

    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=PROJECT_TITLE,
        version=VERSION,
        description=description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore
