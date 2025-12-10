from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
from utils.configuration import ConfigurationWator
import random

class Shark(Fish):
    def __init__(self, pos_x: int, pos_y: int, config: ConfigurationWator)-> None:
        super().__init__(pos_x, pos_y, config)
        self.energy: int = config.energy_shark
        self.reproduction_time: int = config.times_breed_shark
        self.emoji: str ="🦈"
    
    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        if not available_moves:
            return (self.pos_x, self.pos_y)

        if isinstance(grid[available_moves[0][1]][available_moves[0][0]], Tuna):
            x, y = random.choice(available_moves)
            tuna = grid[y][x]
            self.eat(tuna)  
            return (x, y)

        return super().choose_move(available_moves, grid)

    def eat(self, tuna: Tuna) -> None:
        tuna.is_alive = False
        self.energy += self.config.recovery_energy_shark

    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        available: list[tuple[int, int]] = []
        neighbors: list[tuple[int, int]] = self.get_neighbors(grid)
    
        for (x, y) in neighbors:
            cell : Fish | None = grid[y][x]
            if isinstance(cell, Tuna) and cell.is_alive:
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
            self.reproduction_time = self.config.times_breed_shark
            return Shark(pos_x, pos_y, self.config)
        
        self.reproduction_time -= 1
        return None 