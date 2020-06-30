import json
from copy import deepcopy
from typing import List, Union

from pyopentdb.model.Question import Question


class QuestionSet:
    def __init__(self, questions: List[Question]):
        self.items = questions

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, item: int) -> Question:
        return self.items[item]

    def __setitem__(self, key: int, value: Question) -> Question:
        self.items[key] = value
        return value

    def __delitem__(self, key) -> Question:
        item = deepcopy(self.items[key])
        del self.items[key]
        return item

    def __iter__(self) -> Question:
        yield from self.items

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)

    def to_serializable(self, as_json: bool = False) -> Union[List[dict], str]:
        output = [i.to_serializable() for i in self.items]
        if as_json is True:
            return json.dumps(output)
        else:
            return output
