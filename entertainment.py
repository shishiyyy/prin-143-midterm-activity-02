import py_serializable

@py_serializable.serializable_class
class Entertainment:
    def __init__(self, *, title: str, type: str, genre: str, releaseYear: str, rating: str) -> None:
        self._title = title
        self._type = type
        self._genre = genre
        self._releaseYear = releaseYear
        self._rating = rating

    @property
    def title(self) -> str:
        return self._title

    @property
    def type(self) -> str:
        return self._type

    @property
    def genre(self) -> str:
        return self._genre

    @property
    def releaseYear(self) -> str:
        return self._releaseYear

    @property
    def rating(self) -> str:
        return self._rating