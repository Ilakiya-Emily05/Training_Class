from fastapi import FastAPI
from app.middleware.cors import setup_cors

# Import routers
from app.controllers import student_controller, course_controller, enrollment_controller

app = FastAPI(title="LMS API", version="1.0")

# Setup middleware
setup_cors(app)

# Include routers
app.include_router(student_controller.router, prefix="/students", tags=["Students"])
app.include_router(course_controller.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment_controller.router, prefix="/enrollments", tags=["Enrollments"])