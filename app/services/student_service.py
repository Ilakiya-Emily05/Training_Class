from app.repositories.student_repository import StudentRepository
from app.models.student_model import Student

class StudentService:
    def __init__(self, student_repo: StudentRepository):
        self.student_repo = student_repo

    def create_student(self, name: str, email: str) -> Student:
        if self.student_repo.get_student_by_email(email):
            raise ValueError("Email already exists")
        student = Student(name, email)
        return self.student_repo.add_student(student)

    def get_student(self, student_id: int) -> Student:
        student = self.student_repo.get_student_by_id(student_id)
        if not student:
            raise ValueError("Student not found")
        return student

    def list_students(self):
        return self.student_repo.list_students()