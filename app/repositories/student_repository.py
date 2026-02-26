from app.core.db import students_db, get_next_student_id
from app.models.student_model import Student

class StudentRepository:
    def add_student(self, student: Student):
        student.id = get_next_student_id()
        students_db.append(student)
        return student

    def get_student_by_id(self, student_id: int):
        return next((s for s in students_db if s.id == student_id), None)

    def get_student_by_email(self, email: str):
        return next((s for s in students_db if s.email == email), None)

    def list_students(self):
        return students_db