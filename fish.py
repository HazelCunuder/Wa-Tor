class Fish:
    def __init__(self, pos_x, pos_y, breed_time=0):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.breed_time = breed_time

    def move(self, new_x, new_y):
        self.pos_x = new_x
        self.pos_y = new_y

    def  get_available_spaces(self):
        pass

    def reproduce(self):
        pass