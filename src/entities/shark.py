from .fish import Fish
from .tuna import Tuna
from __future__ import annotations

class Shark(Fish):
    def __init__(self, pos_x: int, pos_y: int)-> None:
        super().__init__(pos_x, pos_y)
        self.energy: int = 5
        self.reproduction_time: int = 5
        self.emoji_shark: str ="🦈"
    
    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        available:  list[tuple[int, int]] = []
        neighbors:  list[tuple[int, int]] = self.get_neighbors(grid)
        
        for (x, y) in neighbors:
            if  isinstance(grid[y][x], Tuna):
                available.append((x, y))
        if available:
            self.energy += 2
            return available
        else:
            self.energy -= 1
            return super().get_available_spaces(grid)
        
    def reproduce(self, pos_x: int, pos_y: int) -> Shark | None:
        if self.reproduction_time <= 0:
            self.reproduction_time = 5
            return Shark(pos_x, pos_y)
        
        self.reproduction_time -= 1
        return None