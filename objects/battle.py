from objects.trainer import Trainer


class Battle:
    def __init__(self, player: Trainer, rival: Trainer) -> None:
        self.player = player
        self.rival = rival
