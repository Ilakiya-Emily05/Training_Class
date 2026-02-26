from fastapi import APIRouter, HTTPException
from app.dependencies.dependencies import course_service
from app.schemas.course_schema import CourseCreate, CourseResponse

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.post("/", response_model=CourseResponse, status_code=201)
def create_course(course: CourseCreate):
    return course_service.create_course(course.title, course.duration)

@router.get("/{course_id}", response_model=CourseResponse)
def get_course(course_id: int):
    try:
        return course_service.get_course(course_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/", response_model=list[CourseResponse])
def list_courses():
    return course_service.list_courses()