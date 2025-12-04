import random
from entities.fish import Fish
from entities.tuna import Tuna
from entities.shark import Shark

class World:
    def __init__(self, height: int, width: int) -> None:
        self.grid_height: int = height
        self.grid_width: int = width
        self.grid = self.init_grid()
        self.chronons: int = 0
        self.fishes: list[Fish] = []
        self.tunas: list[Tuna] = []
        self.sharks: list[Shark] = []
        
    def init_grid(self) -> list[list[str]]:
        # We use _ here because we won't use this variable for anything else in the entire code
        return [[" " for _ in range(self.grid_width)] for _ in range(self.grid_height)]
    
    def display_grid(self) -> list[list[str]]:
        display = self.init_grid()
        
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                cell = self.grid[y][x]
                if isinstance(cell, Shark):
                    display[y][x] = cell.emoji_shark
                elif isinstance(cell, Tuna):
                    display[y][x] = cell.emoji
                else:
                    display[y][x] = " "
        return display
    
    def new_tuna(self, tuna: Tuna):
        if not self.is_position_valid(x=tuna.pos_x, y=tuna.pos_y):
            return None
        if len(self.tunas) >= (self.grid_width * self.grid_height):
            return None
        self.tunas.append(tuna)
        self.grid[tuna.pos_y][tuna.pos_x] = tuna
        
    def is_position_valid(self, x: int, y: int) -> bool:
        if x >= self.grid_width or y >= self.grid_height:
            return False
        else:
            if self.grid[y][x] == " ":
                return True
            else:
                return False    
    
    def randomly_place_fishes(self, nb_sharks: int, nb_tunas: int):
        for _ in range(nb_sharks):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
                
                if self.is_position_valid(x=x,y=y):
                    shark = Shark(x, y)
                    self.new_shark(shark)
                    break
        for _ in range(nb_tunas):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
                
                if self.is_position_valid(x=x, y=y):
                    tuna = Tuna(x, y)
                    self.new_tuna(tuna)
                    break
    
    
