import json

from objects.type import Type

_damage_matrix_cache = None


def get_damage_matrix():
    global _damage_matrix_cache
    if _damage_matrix_cache is None:
        with open("resources/damage_matrix.json") as f:
            data = json.load(f)
        _damage_matrix_cache = {int(k): v for k, v in data.items()}
    return _damage_matrix_cache


def get_damage_multiplier(attack_type: Type, defend_type: Type):
    return get_damage_matrix()[attack_type.value][defend_type.value]
