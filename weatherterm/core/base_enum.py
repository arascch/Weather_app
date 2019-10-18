from enum import Enum

class BaseEnum(Enum):
    def _generate_next_value(name , start , count , last_value):
        return name
        