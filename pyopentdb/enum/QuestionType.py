from enum import Enum, unique


@unique
class QuestionType(Enum):
    MULTIPLE = "multiple"
    TRUE_FALSE = "boolean"


question_type_map = {i.value: i for i in QuestionType}
