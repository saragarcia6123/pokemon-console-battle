from objects.player import Player
from objects.pokedex import Pokedex


class Game:
    pokedex = Pokedex().pokedex

    def __init__(self, player_name: str | None = None):
        if not player_name:
            player_name = "Player"
        self.player = Player(name=player_name, party=[])
        self.npc = Player(name="NPC", party=[])
