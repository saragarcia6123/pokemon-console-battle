import math
from models.model_pokemon import ModelPokemon
from objects.natures import get_random_nature, get_stat_multiplier
from objects.pokedex import Pokedex
import random

from objects.stat import STAT, STAT_INDEXES


class Pokemon:

    def __init__(
        self,
        id: int,
        level: int,
        hp: int | None = None,
        xp: int | None = None,
        fainted: bool | None = None,
        move_set: list[str] | None = None,
        ivs: list[int] | None = None,
        evs: list[int] | None = None,
        nature: str | None = None,
    ):
        self.id = id
        self.level = level
        self.model: ModelPokemon = Pokedex().pokedex[self.id]

        if not move_set:
            self.initialize_move_set()
        else:
            self.move_set = move_set[:4]

        if not ivs:
            self.initialize_ivs()
        else:
            self.ivs = ivs

        if not evs:
            self.initialize_evs()
        else:
            self.evs = evs

        if not nature:
            self.nature = get_random_nature()
        else:
            self.nature = nature

        self.set_stats()

        self.hp = hp if hp else self.max_hp
        self.xp = xp if xp else 0
        self.fainted = fainted if fainted else False

    def __str__(self) -> str:
        return f"{self.model.name} (lvl {self.level})"

    def initialize_move_set(self):
        self.move_set = []
        for move, level in self.model.moves.items():
            if level <= self.level and level != 0:
                self.move_set.append(move)
        if len(self.move_set) > 4:
            self.move_set[:] = random.sample(self.move_set, 4)

    def initialize_ivs(self):
        self.ivs: list[int] = [0, 0, 0, 0, 0, 0]
        for i in range(6):
            self.ivs[i] = random.randint(0, 31)

    def initialize_evs(self):
        self.evs: list[int] = [0, 0, 0, 0, 0, 0]

    def set_stats(self):
        self.max_hp = self.calculate_stat("hp")
        self.attack = self.calculate_stat("attack")
        self.defense = self.calculate_stat("defense")
        self.special_attack = self.calculate_stat("special-attack")
        self.special_defense = self.calculate_stat("special-defense")
        self.speed = self.calculate_stat("speed")

    def calculate_stat(self, stat: STAT):
        stat_index = STAT_INDEXES[stat]
        match stat:
            case "hp":
                b = self.model.base_hp
            case "attack":
                b = self.model.base_attack
            case "defense":
                b = self.model.base_defense
            case "special-attack":
                b = self.model.base_special_attack
            case "special-defense":
                b = self.model.base_special_defense
            case "speed":
                b = self.model.base_speed

        i = self.ivs[stat_index]
        e = self.evs[stat_index]
        l = self.level
        n = get_stat_multiplier(self.nature, stat)

        if stat == "hp":
            return math.floor((2 * b + i + e) * l / 100 + l + 10)
        else:
            return math.floor(math.floor((2 * b + i + e) * l / 100 + 5) * n)

    def heal(self, amount: int):
        if self.fainted:
            return
        self.hp = min(self.max_hp, self.hp + amount)

    def damage(self, amount: int):
        self.hp = max(0, self.hp - amount)
        if self.hp == 0:
            self.fainted = True
