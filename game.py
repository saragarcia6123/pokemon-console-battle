from objects.trainer import Trainer
from objects.pokedex import Pokedex


class Game:
    pokedex = Pokedex().pokedex

    def __init__(self, player_name: str | None = None):
        if not player_name or player_name == "":
            player_name = "Red"
        self.player = Trainer(name=player_name, party=[])
        self.rival = Trainer(name="Blue", party=[])
