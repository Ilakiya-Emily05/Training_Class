# app/core/db.py

# In-memory storage
students_db = []
courses_db = []
enrollments_db = []

# ID counters
student_id_counter = 1
course_id_counter = 1
enrollment_id_counter = 1

# Helper functions to get IDs
def get_next_student_id():
    global student_id_counter
    student_id = student_id_counter
    student_id_counter += 1
    return student_id

def get_next_course_id():
    global course_id_counter
    course_id = course_id_counter
    course_id_counter += 1
    return course_id

def get_next_enrollment_id():
    global enrollment_id_counter
    enrollment_id = enrollment_id_counter
    enrollment_id_counter += 1
    return enrollment_id