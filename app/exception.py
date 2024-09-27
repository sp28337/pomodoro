class UserNotFound(Exception):
    detail = "User not found"


class UserIncorrectPassword(Exception):
    detail = "Incorrect password"


class TokenExpired(Exception):
    detail = "Token expired"


class IncorrectToken(Exception):
    detail = "Incorrect token"


class TaskNotFound(Exception):
    detail = "Task not found"
