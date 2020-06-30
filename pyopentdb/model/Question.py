from dataclasses import dataclass
from typing import List
from random import shuffle

from pyopentdb.enum import QuestionType, Difficulty, Category
from pyopentdb.exc import QuestionError


@dataclass
class Question:
    category: Category
    question_type: QuestionType
    difficulty: Difficulty
    question: str
    choices: List[str]
    answer: str
    answer_index: int = None

    def __post_init__(self):
        # Shuffle choices
        shuffle(self.choices)

        # Try to set answer index
        try:
            self.answer_index = self.choices.index(self.answer)
        except ValueError:
            raise QuestionError(
                f"Answer ({self.answer}) is not in the list of choices ({self.choices})"
            )
