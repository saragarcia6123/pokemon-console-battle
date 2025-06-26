from pydantic import BaseModel, Field, field_validator

from objects.type import Type


class ModelPokemon(BaseModel):
    id: int
    name: str
    type_1: Type = Field(alias="type-1")
    type_2: Type | None = Field(alias="type-2", default=None)
    base_xp: int = Field(alias="base-xp")
    base_hp: int = Field(alias="base-hp")
    base_attack: int = Field(alias="base-attack")
    base_defense: int = Field(alias="base-defense")
    base_special_attack: int = Field(alias="base-special-attack")
    base_special_defense: int = Field(alias="base-special-defense")
    base_speed: int = Field(alias="base-speed")
    height: int
    weight: int
    moves: dict[str, int]

    class Config:
        validate_by_name = True

    @field_validator("type_1", "type_2", mode="before")
    @classmethod
    def parse_type(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            try:
                return Type[v.upper()]
            except KeyError:
                raise ValueError(f"Invalid type: {v}")
        return v
