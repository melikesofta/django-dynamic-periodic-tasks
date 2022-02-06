from enum import Enum


class TimeInterval(Enum):
    one_sec = '1 sec'
    ten_sec = '10 sec'
    one_min = '1 min'
    five_mins = '5 mins'
    one_hour = '1 hour'


class SetupStatus(Enum):
    active = 'Active'
    disabled = 'Disabled'
