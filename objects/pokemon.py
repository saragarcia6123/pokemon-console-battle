from objects.pokedex import Pokedex


class Pokemon:

    def __init__(self, id: int, level: int):
        self.id = id
        self.level = level

    def __str__(self) -> str:
        name = Pokedex().pokedex[self.id].name
        return f"{name.capitalize()} (lvl {self.level})"
