from fish import Fish

class Tuna (Fish):
    def __init__(self, pos_x, pos_y, reproduction_time= 0, emoji="🐟"):
        super().__init__(pos_x, pos_y, reproduction_time)
        self.emoji = emoji