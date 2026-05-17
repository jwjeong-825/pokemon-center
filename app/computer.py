from fastapi import APIRouter
from app.schemas import PokemonCreate
from app.database import (
    add_pokemon_db,
    get_pokemon_db,
    get_one_pokemon_db,
    delete_pokemon_by_name_db
)

router = APIRouter(
    tags=["Pokemon Computer"]
)


@router.post(
    "/computer/deposit",
    summary="포켓몬 맡기기",
    description="트레이너의 포켓몬을 PC에 저장합니다."
)
def add_pokemon(pokemon: PokemonCreate):

    add_pokemon_db(pokemon.name, pokemon.level)
    return {
        "message": "Pokemon added successfully"
    }


@router.get(
    "/computer",
    summary="맡긴 포켓몬 전체 조회",
    description="PC에 저장된 모든 포켓몬 목록을 조회합니다."
)
def get_pokemon():

    return get_pokemon_db()


@router.get(
    "/computer/{pokemon_id}",
    summary="포켓몬 상세 조회",
    description="특정 포켓몬의 정보를 조회합니다."
)
def get_one_pokemon(pokemon_id: int):

    pokemon = get_one_pokemon_db(pokemon_id)

    if pokemon is None:
        return {"message": "Pokemon not found"}

    return pokemon


@router.delete(
    "/computer/discharge/{name}",
    summary="포켓몬 찾기",
    description="PC에서 포켓몬을 꺼내 트레이너에게 돌려줍니다."
)
def discharge_pokemon(name: str):

    deleted_count = delete_pokemon_by_name_db(name)

    if deleted_count == 0:
        return {"error": "해당 포켓몬을 찾을 수 없습니다."}

    return {
        "message": f"{name} 퇴원 완료! 트레이너에게 돌아갔습니다."
    }
