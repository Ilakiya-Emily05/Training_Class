class Enrollment:
    def __init__(self, student_id: int, course_id: int):
        self.id: int = 0  # will be set by repository
        self.student_id = student_id
        self.course_id = course_id