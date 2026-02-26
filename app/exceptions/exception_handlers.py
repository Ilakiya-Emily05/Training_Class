from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import NotFoundException, UnauthorizedException

async def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(status_code=404, content={"detail": exc.message})

async def unauthorized_exception_handler(request: Request, exc: UnauthorizedException):
    return JSONResponse(status_code=403, content={"detail": exc.message})