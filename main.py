from utils.console_utils import cls, prompt
from game import Game
from objects.pokemon import Pokemon


cls()

game = Game()

player_name = input("Enter your name: ")
cls()

rival_name = input("Enter rival's name: ")
cls()

game.set_player_name(player_name)
game.set_rival_name(rival_name)

starters = {i: game.pokedex[i].name for i in [1, 4, 7]}
rival_starter_map = {1: 4, 4: 7, 7: 1}

player_starter_id = prompt(
    message="Choose your starter Pokémon",
    choices=[(name.capitalize(), id) for id, name in starters.items()],
)

player_starter_pokemon = Pokemon(id=player_starter_id, level=5)
game.player.party.add_to_party(player_starter_pokemon)

print(
    f"You chose {player_starter_pokemon.model.name}, the {player_starter_pokemon.model.type_1} type Pokémon!"
)

rival_starter_id = rival_starter_map[player_starter_id]
rival_starter_pokemon = Pokemon(id=rival_starter_id, level=5)
game.rival.party.add_to_party(rival_starter_pokemon)

print(
    f"{game.rival.name} chose {rival_starter_pokemon.model.name}, the {rival_starter_pokemon.model.type_1} type Pokémon!"
)

input()

cls()
