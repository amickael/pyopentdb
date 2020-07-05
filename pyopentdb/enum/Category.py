from collections import namedtuple
from enum import Enum, unique

CategoryItem = namedtuple("CategoryItem", ["id", "name", "emoji"])


@unique
class Category(Enum):
    GENERAL_KNOWLEDGE = CategoryItem(9, "General Knowledge", "🧠")
    ENTERTAINMENT_BOOKS = CategoryItem(10, "Entertainment: Books", "📚")
    ENTERTAINMENT_FILM = CategoryItem(11, "Entertainment: Film", "🎞️")
    ENTERTAINMENT_MUSIC = CategoryItem(12, "Entertainment: Music", "🎸")
    ENTERTAINMENT_MUSICALS_THEATRES = CategoryItem(
        13, "Entertainment: Musicals & Theatres", "🎭"
    )
    ENTERTAINMENT_TELEVISION = CategoryItem(14, "Entertainment: Television", "📺")
    ENTERTAINMENT_VIDEO_GAMES = CategoryItem(15, "Entertainment: Video Games", "🕹️")
    ENTERTAINMENT_BOARD_GAMES = CategoryItem(16, "Entertainment: Board Games", "🎲")
    SCIENCE_NATURE = CategoryItem(17, "Science & Nature", "🔬")
    SCIENCE_COMPUTERS = CategoryItem(18, "Science: Computers", "💻")
    SCIENCE_MATHEMATICS = CategoryItem(19, "Science: Mathematics", "🧮")
    MYTHOLOGY = CategoryItem(20, "Mythology", "🔱")
    SPORTS = CategoryItem(21, "Sports", "⚽")
    GEOGRAPHY = CategoryItem(22, "Geography", "🗺️")
    HISTORY = CategoryItem(23, "History", "📜")
    POLITICS = CategoryItem(24, "Politics", "🗳️")
    ART = CategoryItem(25, "Art", "🎨")
    CELEBRITIES = CategoryItem(26, "Celebrities", "💃")
    ANIMALS = CategoryItem(27, "Animals", "🐕")
    VEHICLES = CategoryItem(28, "Vehicles", "🏎️")
    ENTERTAINMENT_COMICS = CategoryItem(29, "Entertainment: Comics", "🦸")
    SCIENCE_GADGETS = CategoryItem(30, "Science: Gadgets", "📱")
    ENTERTAINMENT_JAPANESE_ANIME_MANGA = CategoryItem(
        31, "Entertainment: Japanese Anime & Manga", "🇯🇵"
    )
    ENTERTAINMENT_CARTOON_ANIMATIONS = CategoryItem(
        32, "Entertainment: Cartoon & Animations", "👻"
    )


category_id_map = {i.value.id: i for i in Category}
category_name_map = {i.value.name: i for i in Category}
