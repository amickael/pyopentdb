import requests
from typing import Union, List
from warnings import warn

from pyopentdb.model import Question, QuestionResponse
from pyopentdb.enum import Category, Difficulty, QuestionType, ResponseCode
from pyopentdb.exc import APIError


class OpenTDBClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.params = {"token": self.request_token()}

    @staticmethod
    def request_token() -> str:
        req = requests.get(
            "https://opentdb.com/api_token.php", params={"command": "request"}
        )
        if req.ok:
            return req.json().get("token")

    def reset_token(self):
        req = requests.get(
            f"https://opentdb.com/api_token.php",
            params={"command": "reset", "token": self.session.params.get("token")},
        )
        if req.ok:
            self.session.params.update({"token": req.json().get("token")})

    def get_questions(
        self,
        amount: int = 10,
        category: Union[Category, int] = None,
        difficulty: Union[Difficulty, str] = None,
        question_type: Union[QuestionType, str] = None,
        retry: int = 5,
    ) -> List[Question]:
        # Validate amount
        if not 1 <= amount <= 50:
            raise APIError("Amount must be between 1 and 50, inclusive")

        # Parse enums
        if isinstance(category, Category):
            category = category.value.id
        if isinstance(difficulty, Difficulty):
            difficulty = difficulty.value
        if isinstance(question_type, QuestionType):
            question_type = question_type.value

        # Make HTTP request
        status = 200
        for i in range(retry + 1):
            req = self.session.get(
                "https://opentdb.com/api.php",
                params={
                    "amount": amount,
                    "category": category,
                    "difficulty": difficulty,
                    "type": question_type,
                },
            )
            if req.ok:
                resp = QuestionResponse(**req.json())
                if resp.response_code == ResponseCode.TOKEN_EMPTY:
                    self.reset_token()
                    continue
                elif resp.response_code != ResponseCode.SUCCESS:
                    warn(resp.response_code.value.description)
                return resp.results
            else:
                status = req.status_code
                warn(
                    f"API returned status code {req.status_code}, retrying... ({i}/{retry})"
                )
                continue

        # Raise error if max retries exceeded
        raise APIError(
            f"API returned status code {status}, max retries exceeded, stopping."
        )
