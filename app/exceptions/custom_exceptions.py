class NotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name
        self.message = f"{name} not found"
        super().__init__(self.message)


class UnauthorizedException(Exception):
    def __init__(self):
        self.message = "You are not authorized to perform this action"
        super().__init__(self.message)