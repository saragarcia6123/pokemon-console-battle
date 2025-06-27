from objects.pokemon import Pokemon


class MaxPartyCountError(Exception):
    pass


class MinPartyCountError(Exception):
    pass


class Party:

    def __init__(self, party: list[Pokemon] | None = None):
        if not party:
            party = []
        self.party = party

    def __str__(self) -> str:
        string = ""
        for pokemon in self.party:
            string += pokemon.__str__()
        return string

    def add_to_party(self, pokemon: Pokemon):
        if len(self.party) >= 6:
            raise MaxPartyCountError
        self.party.append(pokemon)

    def remove_from_party(self, index: int):
        if index > len(self.party):
            raise IndexError
        if index == 0:
            raise MinPartyCountError
