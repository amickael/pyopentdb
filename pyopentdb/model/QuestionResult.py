from dataclasses import dataclass
from typing import List
from copy import deepcopy
import html

from pyopentdb.model.Question import Question
from pyopentdb.enum import (
    category_name_map,
    difficulty_map,
    question_type_map,
)
from pyopentdb.exc.QuestionError import QuestionError


@dataclass
class QuestionResult:
    category: str
    type: str
    difficulty: str
    question: str
    correct_answer: str
    incorrect_answers: List[str]

    def __post_init__(self):
        # Unescape all HTML encoded characters
        self.category = html.unescape(self.category)
        self.type = html.unescape(self.type)
        self.difficulty = html.unescape(self.difficulty)
        self.question = html.unescape(self.question)
        self.correct_answer = html.unescape(self.correct_answer)
        self.incorrect_answers = [html.unescape(i) for i in self.incorrect_answers]

    def parse(self) -> Question:
        # Parse values to enums
        category = category_name_map.get(self.category)
        question_type = question_type_map.get(self.type)
        difficulty = difficulty_map.get(self.difficulty)

        # Validate enums
        enums = {
            "Category": [category, self.category],
            "Question Type": [question_type, self.type],
            "Difficulty": [difficulty, self.difficulty],
        }
        for enum, [parsed, original] in enums.items():
            if parsed is None:
                raise QuestionError(f'Invalid {enum} "{original}"')

        # Build Question
        choices = deepcopy(self.incorrect_answers)
        choices.append(self.correct_answer)
        return Question(
            category=category,
            question_type=question_type,
            difficulty=difficulty,
            question=self.question,
            answer=self.correct_answer,
            choices=choices,
        )
