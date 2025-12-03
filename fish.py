class Fish:
    def __init__(self, pos_x, pos_y, ):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def move(self, new_x, new_y):
        self.pos_x = new_x
        self.pos_y = new_y