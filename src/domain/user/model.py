import re
from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any

from domain.user.exceptions import (UnknownAgeException,
                                    WrongPhoneNumberException)


class AgeEnum(StrEnum):
    CHILD = "CHILD"
    TEENAGER = "TEENAGER"
    ADULT = "ADULT"
    UNKNOWN = "UNKNOWN"


@dataclass
class UserDomainModel:
    username: str
    age: int
    email: str
    phone_number: str
    data: dict | None

    @property
    def _prone_number_regex(self) -> str:
        return r"^\+?[78]\d{3} ?\d{3} ?\d{2} ?\d{2}$"

    def _check_phone_number(self) -> bool:
        return re.match(self._prone_number_regex, self.phone_number) is not None

    def verify_phone_number(self) -> None:
        if not self._check_phone_number():
            raise WrongPhoneNumberException(self.phone_number)

    def _check_age(self) -> AgeEnum:
        match self.age:
            case age if 0 <= age < 13:
                return AgeEnum.CHILD
            case age if 13 <= age < 20:
                return AgeEnum.TEENAGER
            case age if 20 <= age:
                return AgeEnum.ADULT
            case _:
                return AgeEnum.UNKNOWN

    def verify_age(self) -> str | None:
        user_age = self._check_age()
        if user_age == AgeEnum.UNKNOWN:
            raise UnknownAgeException(self.age)
        return self._check_age()

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
