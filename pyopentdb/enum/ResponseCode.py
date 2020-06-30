from enum import Enum, unique
from collections import namedtuple

ResponseCodeItem = namedtuple("ResponseCodeItem", ["code", "name", "description"])


@unique
class ResponseCode(Enum):
    SUCCESS = ResponseCodeItem(0, "Success", "Returned results successfully.")
    NO_RESULTS = ResponseCodeItem(
        1,
        "No Results",
        "Could not return results. The API doesn't have enough questions for your query.",
    )
    INVALID_PARAMETER = ResponseCodeItem(
        2,
        "Invalid Parameter",
        "Contains an invalid parameter. Arguments passed in are not valid.",
    )
    TOKEN_NOT_FOUND = ResponseCodeItem(
        3, "Token Not Found", "Session Token does not exist."
    )
    TOKEN_EMPTY = ResponseCodeItem(
        4,
        "Token Empty",
        "Session Token has returned all possible questions for the specified query. Resetting the Token is necessary.",
    )


response_code_map = {i.value.code: i for i in ResponseCode}
