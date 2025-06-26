from pydantic import BaseModel, Field


class ModelPokemon(BaseModel):
    id: int
    name: str
    type_1: str = Field(alias="type-1")
    type_2: str | None = Field(alias="type-2", default=None)
    base_xp: int = Field(alias="base-xp")
    hp: int
    attack: int
    defense: int
    special_attack: int = Field(alias="special-attack")
    special_defense: int = Field(alias="special-defense")
    speed: int
    height: int
    weight: int
    moves: dict[str, int]

    class Config:
        validate_by_name = True
