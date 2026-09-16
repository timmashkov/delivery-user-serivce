class UnknownAgeException(Exception):
    def __init__(self, age: int) -> None:
        self.message = f"Unknown age has been given, age {age} is unreal"
        super().__init__(self.message)


class WrongPhoneNumberException(Exception):
    def __init__(self, phone_number: str) -> None:
        self.message = f"Invalid phone number: {phone_number} has been given"
        super().__init__(self.message)
