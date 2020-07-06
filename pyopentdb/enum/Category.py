from collections import namedtuple
from enum import Enum, unique

CategoryItem = namedtuple("CategoryItem", ["id", "name", "emoji", "aria-label"])


@unique
class Category(Enum):
    GENERAL_KNOWLEDGE = CategoryItem(9, "General Knowledge", "🧠", "brain")
    ENTERTAINMENT_BOOKS = CategoryItem(10, "Entertainment: Books", "📚", "books")
    ENTERTAINMENT_FILM = CategoryItem(11, "Entertainment: Film", "🎞️", "film")
    ENTERTAINMENT_MUSIC = CategoryItem(12, "Entertainment: Music", "🎸", "guitar")
    ENTERTAINMENT_MUSICALS_THEATRES = CategoryItem(
        13, "Entertainment: Musicals & Theatres", "🎭", "masks"
    )
    ENTERTAINMENT_TELEVISION = CategoryItem(
        14, "Entertainment: Television", "📺", "television"
    )
    ENTERTAINMENT_VIDEO_GAMES = CategoryItem(
        15, "Entertainment: Video Games", "🕹️", "joystick"
    )
    ENTERTAINMENT_BOARD_GAMES = CategoryItem(
        16, "Entertainment: Board Games", "🎲", "dice"
    )
    SCIENCE_NATURE = CategoryItem(17, "Science & Nature", "🔬", "microscope")
    SCIENCE_COMPUTERS = CategoryItem(18, "Science: Computers", "💻", "laptop")
    SCIENCE_MATHEMATICS = CategoryItem(19, "Science: Mathematics", "🧮", "abacus")
    MYTHOLOGY = CategoryItem(20, "Mythology", "🔱", "trident")
    SPORTS = CategoryItem(21, "Sports", "⚽", "soccer ball")
    GEOGRAPHY = CategoryItem(22, "Geography", "🗺️", "world map")
    HISTORY = CategoryItem(23, "History", "📜", "scroll")
    POLITICS = CategoryItem(24, "Politics", "🗳️", "ballot box")
    ART = CategoryItem(25, "Art", "🎨", "palette")
    CELEBRITIES = CategoryItem(26, "Celebrities", "📸", "camera")
    ANIMALS = CategoryItem(27, "Animals", "🐕", "dog")
    VEHICLES = CategoryItem(28, "Vehicles", "🏎️", "race car")
    ENTERTAINMENT_COMICS = CategoryItem(29, "Entertainment: Comics", "🦸", "superhero")
    SCIENCE_GADGETS = CategoryItem(30, "Science: Gadgets", "📱", "mobile phone")
    ENTERTAINMENT_JAPANESE_ANIME_MANGA = CategoryItem(
        31, "Entertainment: Japanese Anime & Manga", "🇯🇵", "japanese flag"
    )
    ENTERTAINMENT_CARTOON_ANIMATIONS = CategoryItem(
        32, "Entertainment: Cartoon & Animations", "🐱🐭", "cat and mouse"
    )


category_id_map = {i.value.id: i for i in Category}
category_name_map = {i.value.name: i for i in Category}
