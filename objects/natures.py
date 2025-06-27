import random

from objects.stat import STAT, STAT_INDEXES

nature_matrix: dict[str, list[int]] = {
    "hardy": [0, 0, 0, 0, 0],
    "lonely": [1, -1, 0, 0, 0],
    "brave": [1, 0, 0, 0, -1],
    "adamant": [1, 0, 0, 0, 0],
    "naughty": [1, 0, 0, -1, 0],
    "docile": [0, 0, 0, 0, 0],
    "bold": [-1, 1, 0, 0, 0],
    "relaxed": [0, 1, 0, 0, -1],
    "impish": [0, 1, -1, 0, 0],
    "lax": [0, 1, 0, -1, 0],
    "serious": [0, 0, 0, 0, 0],
    "timid": [-1, 0, 0, 0, 1],
    "hasty": [0, -1, 0, 0, 1],
    "jolly": [0, 0, -1, 0, 1],
    "naive": [0, 0, 0, -1, 1],
    "bashful": [0, 0, 0, 0, 0],
    "modest": [-1, 0, 1, 0, 0],
    "mild": [0, -1, 1, 0, 0],
    "quiet": [0, 0, 1, 0, -1],
    "rash": [0, 0, 1, -1, 0],
    "quirky": [0, 0, 0, 0, 0],
    "calm": [-1, 0, 0, 1, 0],
    "gentle": [0, -1, 0, 1, 0],
    "sassy": [0, 0, 0, 1, -1],
    "careful": [0, 0, -1, 1, 0],
}


def get_stat_multiplier(nature: str, stat: STAT):
    stat_index = STAT_INDEXES[stat]
    bonus = nature_matrix[nature][stat_index - 1]
    return {0: 0, 1: 1.1, -1: 0.9}[bonus]


def get_random_nature():
    natures = list(nature_matrix.keys())
    random_index = random.randint(0, len(natures) - 1)
    return natures[random_index]
