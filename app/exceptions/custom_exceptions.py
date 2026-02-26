class UserNotFoundException(Exception):
    def __init__(self, detail: str = "User not found"):
        self.detail = detail


class JobNotFoundException(Exception):
    def __init__(self, detail: str = "Job not found"):
        self.detail = detail


class ApplicationNotFoundException(Exception):
    def __init__(self, detail: str = "Application not found"):
        self.detail = detail

class NotFoundException(Exception):
    def __init__(self, detail: str = "Resource not found"):
        self.detail = detail


class ConflictException(Exception):
    def __init__(self, detail: str = "Conflict occurred"):
        self.detail = detail