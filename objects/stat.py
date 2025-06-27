from typing import Literal


type STAT = Literal[
    "hp", "attack", "defense", "special-attack", "special-defense", "speed"
]

type STAT_INDEX = Literal[0, 1, 2, 3, 4, 5]

STAT_INDEXES: dict[STAT, STAT_INDEX] = {
    "hp": 0,
    "attack": 1,
    "defense": 2,
    "special-attack": 3,
    "special-defense": 4,
    "speed": 5,
}
