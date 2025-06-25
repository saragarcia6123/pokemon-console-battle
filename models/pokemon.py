import api


class Pokemon:

    def __init__(self, id: int):
        self.id = id

    def __await__(self):
        return self.create().__await__()

    async def create(self):
        data = await api.fetch(f"/pokemon/{self.id}")
        self.name: str = data['name']
        self.base_exp: int = int(data['base_experience'])
        self.height: int = int(data['height'])
        self.weight: int = int(data['weight'])
        self.moves_learned: dict[str, int] = self.parse_moves(data['moves'])
        return self

    def parse_moves(self, moves_data: dict) -> dict[str, int]:
        moves: dict[str, int] = {}
        for move_data in moves_data:
            name = move_data['move']['name']
            level_learnt = int(move_data['version_group_details'][0]['level_learned_at'])
            moves[name] = level_learnt
        return moves

