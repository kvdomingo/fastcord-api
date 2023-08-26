from enum import Enum


class ChannelType(Enum):
    TEXT = "TEXT"
    VOICE = "VOICE"


class AvailabilityStatus(Enum):
    ONLINE = "ONLINE"
    DO_NOT_DISTURB = "DO_NOT_DISTURB"
    IDLE = "IDLE"
    OFFLINE = "OFFLINE"
