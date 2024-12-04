import random
from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/random-pokemon")
async def get_random_pokemon():
    random_id = random.randint(1, 1010)
    url = f"https://pokeapi.co/api/v2/pokemon/{random_id}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            return pokemon_data
        else:
            return {"error": "Failed to fetch Pokémon data"}
