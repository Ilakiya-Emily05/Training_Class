from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.models.enrollment_model import Enrollment

class EnrollmentService:
    def __init__(self, enrollment_repo: EnrollmentRepository, student_repo: StudentRepository, course_repo: CourseRepository):
        self.enrollment_repo = enrollment_repo
        self.student_repo = student_repo
        self.course_repo = course_repo

    def enroll_student(self, student_id: int, course_id: int) -> Enrollment:
        student = self.student_repo.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")

        course = self.course_repo.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found")

        # Check for duplicate enrollment
        existing = [e for e in self.enrollment_repo.list_enrollments()
                    if e.student_id == student_id and e.course_id == course_id]
        if existing:
            raise ValueError("Already enrolled")

        enrollment = Enrollment(student_id, course_id)
        return self.enrollment_repo.add_enrollment(enrollment)

    def get_enrollment(self, enrollment_id: int) -> Enrollment:
        enrollment = self.enrollment_repo.get_enrollment_by_id(enrollment_id)
        if not enrollment:
            raise ValueError("Enrollment not found")
        return enrollment

    def list_enrollments(self):
        return self.enrollment_repo.list_enrollments()

    def get_enrollments_by_student(self, student_id: int):
        return self.enrollment_repo.get_enrollments_by_student(student_id)

    def get_enrollments_by_course(self, course_id: int):
        return self.enrollment_repo.get_enrollments_by_course(course_id)