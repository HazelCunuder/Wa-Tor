from fish import Fish

class Tuna (Fish):
    def __init__(self, pos_x, pos_y, reproduction_time= 0, emoji_tuna="🐟"):
        super().__init__(pos_x, pos_y, reproduction_time)
        self.emoji_tuna : str = emoji_tuna