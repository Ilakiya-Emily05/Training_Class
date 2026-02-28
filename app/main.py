from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.database.base import Base
from app.database.session import engine
from app.middleware.logging import LoggingMiddleware
from app.middleware.exception_handler import (
    http_exception_handler,
    validation_exception_handler,
    unhandled_exception_handler,
)

from app.routers import (
    auth_router,
    superadmin_router,
    itadmin_router,
    manager_router,
    employee_router,
)

app = FastAPI(title="Enterprise Asset Management System")


# Create DB tables
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)


# Middleware
app.add_middleware(LoggingMiddleware)


# Global Exception Handlers
app.add_exception_handler(StarletteHTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, unhandled_exception_handler)


# Routers
app.include_router(auth_router.router)
app.include_router(superadmin_router.router)
app.include_router(itadmin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)


@app.get("/")
def health_check():
    return {"status": "EAMS running"}