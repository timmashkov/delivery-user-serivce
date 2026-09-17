import re
from dataclasses import asdict, dataclass
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from domain.user.exceptions import (UnknownAgeException,
                                    WrongPhoneNumberException)


class AgeCategoryEnum(StrEnum):
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

    def __post_init__(self) -> None:
        self.verify_phone_number()
        self.age_category: str = self.verify_age()
        self.uuid: UUID = uuid4()

    def _check_phone_number(self) -> bool:
        is_valid = re.match(r"^\+?[78]\d{3} ?\d{3} ?\d{2} ?\d{2}$", self.phone_number)
        return is_valid is not None

    def verify_phone_number(self) -> None:
        if not self._check_phone_number():
            raise WrongPhoneNumberException(self.phone_number)

    def _check_age(self) -> AgeCategoryEnum:
        match self.age:
            case age if 0 <= age < 13:
                return AgeCategoryEnum.CHILD
            case age if 13 <= age < 20:
                return AgeCategoryEnum.TEENAGER
            case age if 20 <= age:
                return AgeCategoryEnum.ADULT
            case _:
                return AgeCategoryEnum.UNKNOWN

    def verify_age(self) -> str | None:
        user_age = self._check_age()
        if user_age == AgeCategoryEnum.UNKNOWN:
            raise UnknownAgeException(self.age)
        return self._check_age()

    def to_dict(self) -> dict[str, Any]:
        base_dict = asdict(self)
        base_dict["uuid"] = self.uuid
        return base_dict
