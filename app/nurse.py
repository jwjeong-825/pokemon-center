from fastapi import APIRouter

router = APIRouter()


@router.post("/nurse/heal")
def nurse_heal(name: str, level: int):

    return {
        "message": f"간호사 누나가 {name}을 치료했습니다! 포켓몬을 다시 돌려드립니다.",
        "pokemon": {
            "name": name,
            "level": level,
            "condition": "healthy"
        }
    }
