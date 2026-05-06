from fastapi import FastAPI
from database import (
    create_table,
    add_pokemon_db,
    get_pokemon_db,
    get_one_pokemon_db,
    delete_pokemon_by_name_db
)

app = FastAPI()

create_table()


@app.get("/")
def home():
    return {"message": "Welcome to Juwon's Pokemon Center"}


@app.post("/pokemon")
def add_pokemon(name: str, level: int):
    add_pokemon_db(name, level)

    return {
        "message": "Pokemon added successfully"
    }


@app.get("/pokemon")
def get_pokemon():
    return get_pokemon_db()


@app.get("/pokemon/{pokemon_id}")
def get_one_pokemon(pokemon_id: int):
    pokemon = get_one_pokemon_db(pokemon_id)

    if pokemon is None:
        return {"message": "Pokemon not found"}

    return pokemon


@app.delete("/pokemon/name/{name}")
def discharge_pokemon(name: str):
    deleted_count = delete_pokemon_by_name_db(name)

    if deleted_count == 0:
        return {"error": "해당 포켓몬을 찾을 수 없습니다."}

    return {
        "message": f"{name} 퇴원 완료! 트레이너에게 돌아갔습니다."
    }
