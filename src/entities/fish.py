from networkx import neighbors


class Fish:
    def __init__(self, pos_x: int , pos_y: int)-> None:
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y

    def move(self, grid):
        move: list = self.get_available_spaces(grid)

        print(move)
        pass

    def choose_move(self, available_moves):
        if not available_moves:
            return None
        import random
        return random.choice(available_moves)
    
    def  get_available_spaces(self, grid):
        height:  int = len(grid)
        width:  int = len(grid[0])
        available:  list = []

        neighbors:  list = [
            ((self.pos_x + 1) % width, self.pos_y),
            ((self.pos_x - 1) % width, self.pos_y),
            (self.pos_x, (self.pos_y + 1) % height),
            (self.pos_x, (self.pos_y - 1) % height)
        ]

        for (x, y) in neighbors:
            if grid[y][x] is None:
                available.append((x, y))
        return available

    def reproduce(self):
        pass

fish = Fish(1, 1)
grid = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]

fish.move(grid)