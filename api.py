import aiohttp
import asyncio

API_URL = "https://pokeapi.co/api/v2"

async def fetch(endpoint: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{API_URL}{endpoint}") as response:
            data = await response.json()
            return data

