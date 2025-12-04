from networkx import neighbors
import random

class Fish:
    def __init__(self, pos_x: int , pos_y: int)-> None:
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y

    def move(self, grid: list) -> tuple:
        available_moves : list = self.get_available_spaces(grid)
        move: tuple = self.choose_move(available_moves)
        self.pos_x, self.pos_y = move
        return move

    def choose_move(self, available_moves: list) -> tuple:
        if not available_moves:
            return (self.pos_x, self.pos_y)
        return random.choice(available_moves)
    
    def  get_available_spaces(self, grid: list) -> list:
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