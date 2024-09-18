class UserNotFound(Exception):
    detail = "User not found"


class UserIncorrectPassword(Exception):
    detail = "Incorrect password"
