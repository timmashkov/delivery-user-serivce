from enum import Enum

class EventStatusEnum(Enum):
    WAITING_FOR_SENDING = "WAITING_FOR_SENDING"
    SENT = "SENT"
    CREATED = "CREATED"
    UNSENT = "UNSENT"
    ARCHIVED = "ARCHIVED"
