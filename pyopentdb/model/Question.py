import json
from dataclasses import dataclass, asdict
from enum import Enum
from random import shuffle
from typing import List, Union

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

    def to_serializable(self, as_json: bool = False) -> Union[dict, str]:
        output = {}
        for key, value in asdict(self).items():
            if isinstance(value, Category):
                output[key] = value.value.name
            elif isinstance(value, Enum):
                output[key] = value.value
            else:
                output[key] = value
        if as_json is True:
            return json.dumps(output)
        else:
            return output
