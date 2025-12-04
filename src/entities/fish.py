from __future__ import annotations
import random

class Fish:
    def __init__(self, pos_x: int , pos_y: int)-> None:
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y

    def move(self, grid:  list[list[Fish | None]]) -> tuple[int, int]:
        available_moves : list[tuple[int, int]] = self.get_available_spaces(grid)
        move: tuple[int, int] = self.choose_move(available_moves, grid)
        self.pos_x, self.pos_y = move
        return move

    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        if not available_moves:
            return (self.pos_x, self.pos_y)
        return random.choice(available_moves)
    
    def get_neighbors(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        height:  int = len(grid)
        width:  int = len(grid[0])
        neighbors:  list[tuple[int, int]] = [
            ((self.pos_x + 1) % width, self.pos_y),
            ((self.pos_x - 1) % width, self.pos_y),
            (self.pos_x, (self.pos_y + 1) % height),
            (self.pos_x, (self.pos_y - 1) % height)
        ]
        return neighbors
    
    def  get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        neighbors:  list[tuple[int, int]] = self.get_neighbors(grid)
        available:  list[tuple[int, int]] = []

        for (x, y) in neighbors:
            if grid[y][x] is None :
                available.append((x, y))
        return available

    def reproduce(self, pos_x: int, pos_y: int) -> Fish | None:
        raise NotImplementedError