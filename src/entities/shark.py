from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
import random

class Shark(Fish):
    def __init__(self, pos_x: int, pos_y: int)-> None:
        super().__init__(pos_x, pos_y)
        self.energy: int = 5
        self.reproduction_time: int = 5
        self.emoji_shark: str ="🦈"
        self.is_alive: bool = True
    
    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        if not available_moves:
            return super().choose_move(available_moves)
        
        if isinstance(grid[available_moves[0][1]][available_moves[0][0]], Tuna):
            is_fish = random.choice(available_moves)
            grid[is_fish[1]][is_fish[0]].is_alive = False
            self.energy += 2
            return is_fish

        return super().choose_move(available_moves)
    
    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        available:  list[tuple[int, int]] = []
        neighbors:  list[tuple[int, int]] = self.get_neighbors(grid)
        
        for (x, y) in neighbors:
            if  isinstance(grid[y][x], Tuna) and grid[y][x].is_alive:
                available.append((x, y))
        if available:
            return available
        else:
            self.energy -= 1
            if self.energy <= 0:
                self.is_alive = False
            return super().get_available_spaces(grid)
        
    def reproduce(self, pos_x: int, pos_y: int) -> Shark | None:
        if self.reproduction_time <= 0:
            self.reproduction_time = 5
            return Shark(pos_x, pos_y)
        
        self.reproduction_time -= 1
        return None