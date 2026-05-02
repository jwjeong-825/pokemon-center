from fastapi import FastAPI

app = FastAPI()

pokemon_db = []

@app.get("/")
def home():
    return {"message": "Welcome to Juwon's Pokemon Center"}

@app.post("/pokemon")
def add_pokemon(name: str, level: int):
    pokemon = {
	"id": len(pokemon_db) + 1,
        "name": name,
        "level": level
    }

    pokemon_db.append(pokemon)

    return {
        "message": "Pokemon added successfully",
        "pokemon": pokemon
    }
@app.get("/pokemon")
def get_pokemon():
    return pokemon_db
@app.get("/pokemon/{pokemon_id}")
@app.get("/pokemon/{pokemon_id}")
def get_one_pokemon(pokemon_id: int):
    if pokemon_id <= 0 or pokemon_id > len(pokemon_db):
        return {"message": "Pokemon not found"}

    return pokemon_db[pokemon_id - 1]
