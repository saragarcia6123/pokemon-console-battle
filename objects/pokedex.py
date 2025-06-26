import json

from models.model_pokemon import ModelPokemon
from utils.singleton import singleton


@singleton
class Pokedex:

    pokedex: dict[int, ModelPokemon]

    def __init__(self):
        self.pokedex = {}
        with open("resources/pokedex.json") as f:
            data = json.load(f)

        for i in range(1, len(data) + 1):
            self.pokedex[i] = ModelPokemon(**data[str(i)])
