import random
from entities.fish import Fish
from entities.tuna import Tuna
# from entities.shark import Shark

class World:
    def __init__(self, height: int, width: int) -> None:
        self.grid_height: int = height
        self.grid_width: int = width
        self.grid = self.init_grid()
        self.chronons: int = 0
        self.fishes: list[Fish] = []
        self.tunas: list[Fish] = []
        # self.sharks: list[Shark] = []
        
    def init_grid(self) -> list[list[Fish | None]]:
        # We use _ here because we won't use this variable for anything else in the entire code
        return [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
    
    def display_grid(self) -> list[list[str]]:
        display = [[" " for _ in range(self.grid_width)] for _ in range(self.grid_height)]
        
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                cell = self.grid[y][x]
                #if isinstance(cell, Shark):
                    #display[y][x] = cell.emoji_shark
                if isinstance(cell, Tuna):
                    display[y][x] = cell.emoji_tuna
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
            if self.grid[y][x] == None:
                return True
            else:
                return False    
    
    def randomly_place_fishes(self, nb_sharks: int, nb_tunas: int):
        # for _ in range(nb_sharks):
        #     while True:
        #         x = random.randrange(self.grid_width)
        #         y = random.randrange(self.grid_height)
                
        #         if self.is_position_valid(x=x,y=y):
        #             shark = Shark(x, y)
        #             self.new_shark(shark)
        #             break
        for _ in range(nb_tunas):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
                
                if self.is_position_valid(x=x, y=y):
                    tuna = Tuna(x, y)
                    self.new_tuna(tuna)
                    break
    
    def run_simulation(self):
        new_tunas: list[Fish] = []
      
        for tuna in self.tunas:
            if tuna:
                old_x = tuna.pos_x
                old_y = tuna.pos_y
                new_pos = tuna.move(self.grid)
                self.grid[old_y][old_x] = None
                self.grid[new_pos[1]][new_pos[0]] = tuna
                baby_tuna = tuna.reproduce(pos_x = old_x, pos_y = old_y)
                if baby_tuna and self.is_position_valid(x = baby_tuna.pos_x, y = baby_tuna.pos_y):
                    self.grid[baby_tuna.pos_y][baby_tuna.pos_x] = baby_tuna
                    new_tunas.append(baby_tuna)        
      
        self.tunas.extend(new_tunas)
        self.chronons += 1
        
    def print_grid_ascii(self):
        visual = self.display_grid()
      
        # Top border
        print("+" + ("---+" * len(visual[0])))
      
        # Rows
        for row in visual:
            print("|", end="")
            for cell in row:
                print(f" {cell} |", end="")
            print()
            print("+" + ("---+" * len(visual[0])))
