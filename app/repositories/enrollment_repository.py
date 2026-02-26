from app.core.db import enrollments_db, get_next_enrollment_id
from app.models.enrollment_model import Enrollment

class EnrollmentRepository:
    def add_enrollment(self, enrollment: Enrollment):
        enrollment.id = get_next_enrollment_id()
        enrollments_db.append(enrollment)
        return enrollment

    def list_enrollments(self):
        return enrollments_db

    def list_by_student(self, student_id: int):
        return [e for e in enrollments_db if e.student_id == student_id]

    def list_by_course(self, course_id: int):
        return [e for e in enrollments_db if e.course_id == course_id]

    def exists(self, student_id: int, course_id: int):
        return any(e for e in enrollments_db if e.student_id == student_id and e.course_id == course_id)