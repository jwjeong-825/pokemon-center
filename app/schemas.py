from pydantic import BaseModel, Field


class PokemonCreate(BaseModel):
    name: str = Field(..., example="Pikachu")
    level: int = Field(..., example=15)
