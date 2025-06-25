import asyncio
import aiohttp
import time
import json


async def fetch(endpoint: str) -> dict:
    API_URL = "https://pokeapi.co/api/v2"
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}{endpoint}") as response:
            data = await response.json()
            return data


def parse_moves(moves_data: dict):
    moves: dict[str, int] = {}
    for move_data in moves_data:
        name = move_data["move"]["name"]
        level_learnt = int(move_data["version_group_details"][0]["level_learned_at"])
        if level_learnt > 0:
            moves[name] = level_learnt
    return dict(sorted(moves.items(), key=lambda x: x[1]))


def parse_data(data):
    parsed = {}
    parsed["name"] = data["name"]
    parsed["base_exp"] = int(data["base_experience"])
    parsed["height"] = int(data["height"])
    parsed["weight"] = int(data["weight"])
    parsed["moves_learned"] = parse_moves(data["moves"])
    return parsed


async def create_pokedex(id_from: int = 1, id_to: int = 9):
    pokedex = {}
    for id in range(id_from, id_to + 1):
        data = await fetch(f"/pokemon/{id}")
        pokedex[id] = parse_data(data)
        time.sleep(0.1)
    return pokedex


def write_pokedex_to_json(pokedex):
    j = json.dumps(pokedex, indent=4)
    with open("pokedex.json", "w") as f:
        print(j, file=f)


async def main():
    pokedex = await create_pokedex()
    write_pokedex_to_json(pokedex)


if __name__ == "__main__":
    asyncio.run(main())
