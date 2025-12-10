from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
from .shark import Shark
import random

class Megalodon(Fish):
    def __init__(self,pos_x:int, pos_y:int) -> None:
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.config = None 
    
        self.energy: int = 3
        self.reproduction_time: int = 10
        self.emoji_megalodon: str ="🐋"
        self.is_alive: bool = True


    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        neighbors = self.get_neighbors(grid)
        preys = []
        empty_box = []
    
        for (x, y) in neighbors:
            cell = grid[y][x]
        
        
            if cell is None:  
                empty_box.append((x, y))
        
        
            elif isinstance(cell, (Tuna, Shark)) and cell.is_alive:  
                preys.append((x, y))
        
    
        if preys:
            return preys 
        elif empty_box:
            self.energy -= 1
            return empty_box  
        else:
            self.energy -= 1
            return []
    

    


    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        if not available_moves:
            return (self.pos_x, self.pos_y)
        
        x, y = random.choice(available_moves)
        target = grid[y][x]
        
        if isinstance(target, (Tuna, Shark)) and target.is_alive:
            self.eat(grid, x, y)
        
        return (x, y)



    def eat(self, grid: list[list[Fish | None]],pos_x:int, pos_y:int) -> bool:
        target = grid[pos_y][pos_x]
        if isinstance(target, (Tuna, Shark)) and not isinstance(target, Megalodon):
            self.energy += 1 
            target.is_alive = False 
        

    def reproduce(self, pos_x: int, pos_y: int) -> Fish | None:
        if self.reproduction_time <= 0:
            self.reproduction_time = 10
            return Megalodon(pos_x, pos_y)
        self.reproduction_time -= 1
        return None
    