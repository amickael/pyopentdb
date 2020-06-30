from typing import List

from pyopentdb.enum import response_code_map
from pyopentdb.model.QuestionResult import QuestionResult
from pyopentdb.model.QuestionSet import QuestionSet


class QuestionResponse:
    def __init__(self, response_code: int, results: List[dict]):
        self.response_code = response_code_map.get(response_code)
        self.results = QuestionSet([QuestionResult(**i).parse() for i in results])
