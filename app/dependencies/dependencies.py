from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.repositories.enrollment_repository import EnrollmentRepository

from app.services.student_service import StudentService
from app.services.course_service import CourseService
from app.services.enrollment_service import EnrollmentService

# Single instances for the whole app (in-memory DB)
student_repo = StudentRepository()
course_repo = CourseRepository()
enrollment_repo = EnrollmentRepository()

# Services using those repos
student_service = StudentService(student_repo)
course_service = CourseService(course_repo)
enrollment_service = EnrollmentService(enrollment_repo, student_repo, course_repo)