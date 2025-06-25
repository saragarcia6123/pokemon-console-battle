from models.pokemon import Pokemon
import time

class Pokedex:

    def __init__(self):
        self.pokedex: dict[int, Pokemon] = {}

    def __await__(self):
        return self.create().__await__()
    
    async def create(self):
        for id in range(1, 10):
            p = await Pokemon(id)
            self.pokedex[id] = p
            time.sleep(0.1)
        return self

