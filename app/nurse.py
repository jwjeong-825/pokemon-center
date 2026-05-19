from fastapi import APIRouter

router = APIRouter(
    tags=["Nurse"]
)


@router.post("/heal")
def heal_pokemon():

    return {
        "message": "포켓몬이 모두 완전히 회복되었습니다!"
    }
