class Course:
    def __init__(self, title: str, duration: int):
        self.id: int = 0  # will be set by repository
        self.title = title
        self.duration = duration  # in hours