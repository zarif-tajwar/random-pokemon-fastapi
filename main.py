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
            return {
                "id": pokemon_data["id"],
                "name": pokemon_data["name"],
                "types": [type["type"]["name"] for type in pokemon_data["types"]],
                "abilities": [
                    ability["ability"]["name"] for ability in pokemon_data["abilities"]
                ],
            }
        else:
            return {"error": "Failed to fetch Pokémon data"}
