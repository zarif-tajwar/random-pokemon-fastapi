# Random Pokémon Info API

A simple FastAPI application that fetches information about a random Pokémon using the [PokéAPI](https://pokeapi.co/).

## Features

- Fetch details about a random Pokémon (name, ID, types, and abilities).
- Lightweight and minimal setup.
- Asynchronous HTTP requests for concurrency.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/zarif-tajwar/random-pokemon-fastapi.git
```

2. cd into the cloned repo:

```
cd random-pokemon-fastapi
```

3. Create a virtual environment:

```bash
python -m venv .venv
```

4. Activate the virtual environment:

```bash
# Windows Powershell
.venv\Scripts\Activate.ps1

# Linux or Mac
source .venv/bin/activate

```

5. Install the requirements:

```bash
pip install -r requirements.txt
```

6. Run the dev server:

```bash
fastapi dev main.py
```
