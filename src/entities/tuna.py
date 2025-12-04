from .fish import Fish

class Tuna (Fish):
    def __init__(self, pos_x: int, pos_y: int)-> None:
        super().__init__(pos_x, pos_y)
        self.reproduction_time: int = 3
        self.emoji_tuna: str ="🐟"

    def reproduce(self, pos_x: int, pos_y: int) -> Fish | None:
        if self.reproduction_time <= 0:
            self.reproduction_time = 3
            return Tuna(pos_x, pos_y)
        
        self.reproduction_time -= 1
        return None