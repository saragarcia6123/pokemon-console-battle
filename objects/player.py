from objects.party import Party
from objects.pokemon import Pokemon


class Player:

    def __init__(self, name: str, party: list[Pokemon] | None):
        self.name = name
        self.party = Party(party)
