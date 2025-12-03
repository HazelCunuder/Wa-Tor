import random

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
                    display[y][x] = cell.emoji_fish
                else:
                    display[y][x] = " "
        return display
    
     def new_tuna(self, tuna: Tuna):
        if not self.is_position_valid(x=tuna.x, y=tuna.y):
            return None
        if len(self.tunas) >= (self.grid_width * self.grid_height):
            return None
        self.tunas.append(tuna)
        self.grid[fish.y][fish.x] = fish
        
    def is_position_valid(self, x: int, y: int) -> bool:
        if x >= self.grid_width or y >= self.grid_height:
            return False
        else:
            if self.grid[y][x] == " ":
                return True
            else:
                return False    
    
    