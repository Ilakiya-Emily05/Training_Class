from app.core.db import courses_db, get_next_course_id
from app.models.course_model import Course

class CourseRepository:
    def add_course(self, course: Course):
        course.id = get_next_course_id()
        courses_db.append(course)
        return course

    def get_course_by_id(self, course_id: int):
        return next((c for c in courses_db if c.id == course_id), None)

    def list_courses(self):
        return courses_db