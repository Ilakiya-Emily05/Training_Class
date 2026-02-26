from fastapi import Request
from fastapi.responses import JSONResponse
from starlette import status

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    JobNotFoundException,
    ApplicationNotFoundException
)


def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": exc.detail},
    )


def job_not_found_handler(request: Request, exc: JobNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": exc.detail},
    )


def application_not_found_handler(request: Request, exc: ApplicationNotFoundException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"error": exc.detail},
    )