from .fish import Fish

class Tuna (Fish):
    def __init__(self, pos_x: int, pos_y: int)-> None:
        super().__init__(pos_x, pos_y)
        self.reproduction_time: int = 3
        self.emoji_tuna: str ="🐟"