from enum import IntEnum


class Level(IntEnum):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class RepUnit(IntEnum):
    REPS = 1
    SECONDS = 2

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
