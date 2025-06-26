from typing import Literal
from pydantic import BaseModel, Field

from objects.type import Type


class ModelMove(BaseModel):
    id: int
    name: str
    accuracy: int
    effect_chance: int | None
    pp: int
    priority: int
    power: int
    damage_class: Literal["status", "physical", "special"]
    type: Type
