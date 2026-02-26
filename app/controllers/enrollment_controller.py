from fastapi import APIRouter, HTTPException
from app.dependencies.dependencies import enrollment_service
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

@router.post("/", response_model=EnrollmentResponse, status_code=201)
def enroll_student(enrollment: EnrollmentCreate):
    try:
        return enrollment_service.enroll_student(enrollment.student_id, enrollment.course_id)
    except ValueError as e:
        msg = str(e)
        if msg == "Already enrolled":
            raise HTTPException(status_code=400, detail=msg)
        elif msg in ["Student not found", "Course not found"]:
            raise HTTPException(status_code=404, detail=msg)
        raise HTTPException(status_code=400, detail=msg)

@router.get("/", response_model=list[EnrollmentResponse])
def list_enrollments():
    return enrollment_service.list_enrollments()