class Student:
    def __init__(self, name: str, email: str):
        self.id: int = 0  # will be set by repository
        self.name = name
        self.email = email