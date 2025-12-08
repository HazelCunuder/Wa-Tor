import random
from entities.fish import Fish
from entities.tuna import Tuna
from entities.shark import Shark
from utils.configuration import ConfigurationWator

class World:
    def __init__(self, height: int, width: int) -> None:
        self.grid_height: int = height
        self.grid_width: int = width
        self.grid_size: int = height * width
        self.grid = self.init_grid()
        self.chronons: int = 0
        self.fishes: list[Fish] = []
        self.tunas: list[Tuna] = []
        self.sharks: list[Shark] = []
        self.config: ConfigurationWator = ConfigurationWator()
        
    def init_grid(self) -> list[list[Fish | None]]:
        # We use _ here because we won't use this variable for anything else in the entire code
        return [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
    
    def new_tuna(self, tuna: Tuna):
        if not self.is_position_valid(x=tuna.pos_x, y=tuna.pos_y):
            return None
        if len(self.tunas) >= (self.grid_width * self.grid_height):
            return None
        self.tunas.append(tuna)
        self.fishes.append(tuna)
        self.grid[tuna.pos_y][tuna.pos_x] = tuna
        
    def new_shark(self, shark: Shark):
        if not self.is_position_valid(x=shark.pos_x, y=shark.pos_y):
            return None
        if len(self.tunas) >= (self.grid_width * self.grid_height):
            return None
        self.sharks.append(shark)
        self.fishes.append(shark)
        self.grid[shark.pos_y][shark.pos_x] = shark
        
    def is_position_valid(self, x: int, y: int) -> bool:
        if x >= self.grid_width or y >= self.grid_height:
            return False
        else:
            if self.grid[y][x] == None:
                return True
            else:
                return False    
    
    def randomly_place_fishes(self, nb_sharks: int, nb_tunas: int):
        
        for _ in range(nb_sharks):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
              
                if self.is_position_valid(x=x,y=y):
                    shark = Shark(x, y, self.config)
                    self.new_shark(shark)
                    break
                
        for _ in range(nb_tunas):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
                
                if self.is_position_valid(x=x, y=y):
                    tuna = Tuna(x, y, self.config)
                    self.new_tuna(tuna)
                    break
    
    def world_cycle(self):
        new_sharks: list[Shark] = []
        new_tunas: list[Tuna] = []    
    
        for shark in self.sharks:
            if shark and shark.is_alive:
                old_x = shark.pos_x
                old_y = shark.pos_y
                new_pos = shark.move(self.grid)
                self.grid[old_y][old_x] = None
                self.grid[new_pos[1]][new_pos[0]] = shark
                baby_shark = shark.reproduce(pos_x= old_x, pos_y= old_y)
                if baby_shark and self.is_position_valid(x= baby_shark.pos_x, y= baby_shark.pos_y):
                    self.grid[baby_shark.pos_y][baby_shark.pos_x] = baby_shark
                    new_sharks.append(baby_shark)
            if shark and not shark.is_alive:
                old_x = shark.pos_x
                old_y = shark.pos_y
                self.grid[old_y][old_x] = None
                self.sharks.remove(shark)
                self.fishes.remove(shark)

        for tuna in self.tunas:
            if tuna and tuna.is_alive:
                old_x = tuna.pos_x
                old_y = tuna.pos_y
                new_pos = tuna.move(self.grid)
                self.grid[old_y][old_x] = None
                self.grid[new_pos[1]][new_pos[0]] = tuna
                baby_tuna = tuna.reproduce(pos_x = old_x, pos_y = old_y)
                if baby_tuna and self.is_position_valid(x = baby_tuna.pos_x, y = baby_tuna.pos_y):
                    self.grid[baby_tuna.pos_y][baby_tuna.pos_x] = baby_tuna
                    new_tunas.append(baby_tuna)
            if tuna and not tuna.is_alive:
                old_x = tuna.pos_x
                old_y = tuna.pos_y
                self.grid[old_y][old_x] = None
                self.tunas.remove(tuna)
                self.fishes.remove(tuna)

        self.sharks.extend(new_sharks)
        self.tunas.extend(new_tunas)
        
        self.fishes.extend(new_sharks)
        self.fishes.extend(new_tunas)
        
        self.chronons += 1

