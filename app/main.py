from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Middleware imports
from app.middleware.logging_middleware import logging_middleware
from app.middleware.cors import add_cors_middleware

# Exception imports
from app.exceptions.exception_handlers import (
    not_found_exception_handler,
    unauthorized_exception_handler
)
from app.exceptions.custom_exceptions import NotFoundException, UnauthorizedException

# Router imports
from app.controllers.user_controller import router as user_router
from app.controllers.product_controller import router as product_router
from app.controllers.application_controller import router as application_router
from app.controllers.repayment_controller import router as repayment_router

# Database
from app.core.database import engine

# Create FastAPI instance
app = FastAPI(title="Banking LMS API", version="1.0")

# Add middleware
add_cors_middleware(app)  # CORS
app.middleware("http")(logging_middleware)  # Logging

# Add custom exception handlers
app.add_exception_handler(NotFoundException, not_found_exception_handler)
app.add_exception_handler(UnauthorizedException, unauthorized_exception_handler)

# Include routers
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(product_router, prefix="/loan-products", tags=["Loan Products"])
app.include_router(application_router, prefix="/loan-applications", tags=["Loan Applications"])
app.include_router(repayment_router, prefix="/repayments", tags=["Repayments"])

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Banking Loan Management System API"}

# Startup event
@app.on_event("startup")
def startup_event():
    try:
        with engine.connect() as conn:
            print("Database connected successfully!")
    except Exception as e:
        print("Database connection failed:", e)