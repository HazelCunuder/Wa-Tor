from fish import Fish

class Tuna (Fish):
    def __init__(self, pos_x, pos_y, emoji_tuna="🐟"):
        super().__init__(pos_x, pos_y)
        self.emoji_tuna : str = emoji_tuna
        self.reproduction_time: int = 3