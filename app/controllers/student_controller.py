from fastapi import APIRouter, HTTPException
from app.dependencies.dependencies import student_service
from app.schemas.student_schema import StudentCreate, StudentResponse

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=StudentResponse, status_code=201)
def create_student(student: StudentCreate):
    try:
        s = student_service.create_student(student.name, student.email)
        return s
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{student_id}", response_model=StudentResponse)
def get_student(student_id: int):
    try:
        s = student_service.get_student(student_id)
        return s
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))