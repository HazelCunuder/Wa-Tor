from fish import Fish

class tuna (Fish):
    def __init__(self, pos_x, pos_y, breed_time= 0, emoji="🐟"):
        super().__init__(pos_x, pos_y, breed_time)
        self.emoji = emoji