from fastapi import FastAPI

from app.controllers.user_controller import router as user_router
from app.controllers.job_controller import router as job_router
from app.controllers.application_controller import router as application_router

from app.middleware.cors import add_cors_middleware
from app.middleware.logging import logging_middleware

from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    JobNotFoundException,
    ApplicationNotFoundException,
)

from app.exceptions.exception_handlers import (
    user_not_found_handler,
    job_not_found_handler,
    application_not_found_handler,
)

app = FastAPI(title="Hiring API")

# Middleware
add_cors_middleware(app)
app.middleware("http")(logging_middleware)

# Exception Handlers
app.add_exception_handler(UserNotFoundException, user_not_found_handler)
app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(ApplicationNotFoundException, application_not_found_handler)

# Routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(job_router, prefix="/jobs", tags=["Jobs"])
app.include_router(application_router, prefix="/applications", tags=["Applications"])

@app.get("/")
def root():
    return {"message": "Hiring Application API is alive"}