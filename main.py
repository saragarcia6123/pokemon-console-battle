from utils.console_utils import cls, prompt
from game import Game
from objects.pokemon import Pokemon


cls()

game = Game()

name = input("Enter your name: ")
cls()

game.player.name = name

starters = {i: game.pokedex[i].name for i in [1, 4, 7]}

player_starter_id = prompt(
    message="Choose your starter Pokémon",
    choices=[(name.capitalize(), id) for id, name in starters.items()],
)

player_starter_pokemon = Pokemon(id=player_starter_id, level=5)
game.player.party.add_to_party(player_starter_pokemon)

npc_starter_id = {1: 4, 4: 7, 7: 1}[player_starter_id]
npc_starter_pokemon = Pokemon(id=npc_starter_id, level=5)
game.npc.party.add_to_party(npc_starter_pokemon)

input()

cls()
