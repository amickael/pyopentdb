[![GitHub issues](https://img.shields.io/github/issues/amickael/pyopentdb)](https://github.com/amickael/pyopentdb/issues)
![PyPI](https://img.shields.io/pypi/v/pyopentdb?color=blue)
![PyPI - Downloads](https://img.shields.io/pypi/dw/pyopentdb?color=red)
[![GitHub license](https://img.shields.io/github/license/amickael/pyopentdb?color=purple)](https://github.com/amickael/pyopentdb/blob/master/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# pyopentdb
Python interface for the Open Trivia DB API

## 👶 Dependencies
* [Python 3.6 or higher](https://www.python.org/downloads/)

## 🛠️ Installation
Install from PyPI using `pip`, you may need to use `pip3` depending on your installation
```sh
pip install pyopentdb
```

## 🚀 Quick Start
To get started create an instance of `OpenTDBClient`. Helper enums are provided to make querying easier. Using these enums is not required, you may also pass the standard identifiers as integers/strings. Please see the [API documentation](https://opentdb.com/api_config.php) for more information.



A session token is automatically generated when the object is initialized. The client will also attempt to automatically recycle the token when it expires or runs out of new questions.

Calling `.get_questions()` will return a `QuestionSet` object of `Question` objects. `QuestionSet` is a thin wrapper around a list that provides some additional convenience methods.

```python
from pyopentdb import OpenTDBClient, Category, QuestionType, Difficulty

client = OpenTDBClient()
questions = client.get_questions(
    amount=5,
    category=Category.SCIENCE_NATURE,
    question_type=QuestionType.MULTIPLE,
    difficulty=Difficulty.MEDIUM
)
```

```python
>>> questions
[
  Question(category=<Category.SCIENCE_NATURE: CategoryItem(id=17, name='Science & Nature')>, question_type=<QuestionType.MULTIPLE: 'multiple'>, difficulty=<Difficulty.MEDIUM: 'medium'>, question='All the following metal elements are liquids at or near room temperature EXCEPT:', choices=['Mercury', 'Caesium', 'Gallium', 'Beryllium'], answer='Beryllium', answer_index=3),
  Question(category=<Category.SCIENCE_NATURE: CategoryItem(id=17, name='Science & Nature')>, question_type=<QuestionType.MULTIPLE: 'multiple'>, difficulty=<Difficulty.MEDIUM: 'medium'>, question='The medical condition osteoporosis affects which part of the body?', choices=['Skin', 'Heart', 'Brain', 'Bones'], answer='Bones', answer_index=3),
  Question(category=<Category.SCIENCE_NATURE: CategoryItem(id=17, name='Science & Nature')>, question_type=<QuestionType.MULTIPLE: 'multiple'>, difficulty=<Difficulty.MEDIUM: 'medium'>, question='About how old is Earth?', choices=['4.5 Billion Years', '3.5 Billion Years', '5.5 Billion Years', '2.5 Billion Years'], answer='4.5 Billion Years', answer_index=0),
  Question(category=<Category.SCIENCE_NATURE: CategoryItem(id=17, name='Science & Nature')>, question_type=<QuestionType.MULTIPLE: 'multiple'>, difficulty=<Difficulty.MEDIUM: 'medium'>, question='What do you study if you are studying entomology?', choices=['the Brain', 'Fish', 'Humans', 'Insects'], answer='Insects', answer_index=3),
  Question(category=<Category.SCIENCE_NATURE: CategoryItem(id=17, name='Science & Nature')>, question_type=<QuestionType.MULTIPLE: 'multiple'>, difficulty=<Difficulty.MEDIUM: 'medium'>, question='Which of the following men does not have a chemical element named after him?', choices=['Albert Einstein', 'Enrico Fermi', 'Sir Isaac Newton', 'Niels Bohr'], answer='Sir Isaac Newton', answer_index=2)
]
```

Question choices are shuffled on each call. The `answer_index` field is provided to easily check the correct answer in the choice list.

Both `Question` and `QuestionSet` provide the `.to_serializable` method, which returns either an easily serializable output or a JSON formatted string.
