from typing import Union
from warnings import warn

import requests

from pyopentdb.enum import Category, Difficulty, QuestionType, ResponseCode
from pyopentdb.exc import APIError
from pyopentdb.model import QuestionResponse, QuestionSet


class OpenTDBClient:
    def __init__(self):
        self.session = requests.Session()
        self.request_token()

    def request_token(self):
        req = requests.get(
            "https://opentdb.com/api_token.php", params={"command": "request"}
        )
        if req.ok:
            self.session.params.update({"token": req.json().get("token")})

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
    ) -> QuestionSet:
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
                elif resp.response_code == ResponseCode.TOKEN_NOT_FOUND:
                    self.request_token()
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

    def get_question_count(self, category: Union[Category, int] = None) -> dict:
        if category is None:
            req = self.session.get("https://opentdb.com/api_count_global.php")
        else:
            if isinstance(category, Category):
                category = category.value.id
            req = self.session.get(
                "https://opentdb.com/api_count.php", params={"category": category}
            )
        if req.ok:
            return req.json()
