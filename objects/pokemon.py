from objects.pokedex import Pokedex


class Pokemon:

    def __init__(self, id: int, level: int, move_set: list[str] | None = None):
        self.id = id
        self.level = level
        if not move_set:
            move_set = self.initialize_move_set()
        self.move_set = move_set[:5]

    def __getattr__(self, name):
        return getattr(Pokedex().pokedex[self.id], name)

    def __str__(self) -> str:
        return f"{self.name} (lvl {self.level})"

    def initialize_move_set(self) -> list[str]:
        moves = []
        for move, level in Pokedex().pokedex[self.id].moves.items():
            if level >= self.level and level != 0:
                moves.append(move)
        return moves
