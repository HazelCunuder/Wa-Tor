from fish import Fish

class tuna (Fish):
    def __init__(self, pos_x, pos_y, emojy="🐟", breed_time= 0):
        super().__init__(pos_x, pos_y)
        self.emojy = emojy
        self.breed_time = breed_time