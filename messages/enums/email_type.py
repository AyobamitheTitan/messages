from enum import Enum

class EmailType(int, Enum):
    ONBOARDING = 1
    CODE = 2
    BIRTHDAY = 3
    PASSWORD_RESET = 4
    PASSWORD_RESET_CODE = 5
    EXPIRED_EXCHANGE = 6
    COMPLETED_EXCHANGE = 7
    PROFILE_CHANGE = 8
    PAID_EXCHANGE = 9