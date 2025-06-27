from objects.party import Party
from objects.trainer import Trainer
from objects.pokedex import Pokedex


class Game:
    pokedex = Pokedex().pokedex

    DEFAULT_PLAYER_NAME = "RED"
    DEFAULT_RIVAL_NAME = "BLUE"

    def __init__(
        self, player_name: str = DEFAULT_PLAYER_NAME, rival_name=DEFAULT_RIVAL_NAME
    ):
        self.player = Trainer(name=player_name, party=Party())
        self.rival = Trainer(name=rival_name, party=Party())

    def set_player_name(self, name: str):
        if name == "":
            name = self.DEFAULT_PLAYER_NAME
        self.player.name = name

    def set_rival_name(self, name: str):
        if name == "":
            name = self.DEFAULT_RIVAL_NAME
        self.rival.name = name
