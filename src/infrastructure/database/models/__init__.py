from typing import TypeVar

from ._base import _Base
from .user import User

table = TypeVar(
    "table",
)

__all__: tuple[str] = ("User", "_Base", "table")
