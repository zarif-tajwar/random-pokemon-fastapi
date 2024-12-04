from fastapi import FastAPI

app = FastAPI()


@app.get("/random-pokemon")
async def get_random_pokemon():
    return
