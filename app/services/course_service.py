from app.repositories.course_repository import CourseRepository
from app.models.course_model import Course

class CourseService:
    def __init__(self, course_repo: CourseRepository):
        self.course_repo = course_repo

    def create_course(self, title: str, duration: int) -> Course:
        if self.course_repo.get_course_by_title(title):
            raise ValueError("Course already exists")
        course = Course(title, duration)
        return self.course_repo.add_course(course)

    def get_course(self, course_id: int) -> Course:
        course = self.course_repo.get_course_by_id(course_id)
        if not course:
            raise ValueError("Course not found")
        return course

    def list_courses(self):
        return self.course_repo.list_courses()