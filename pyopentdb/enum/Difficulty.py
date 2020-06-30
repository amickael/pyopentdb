from enum import Enum, unique


@unique
class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


difficulty_map = {i.value: i for i in Difficulty}
