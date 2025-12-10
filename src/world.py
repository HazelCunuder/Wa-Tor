import random
from entities.fish import Fish
from entities.tuna import Tuna
from entities.shark import Shark
from entities.megalodon import Megalodon
from utils.configuration import ConfigurationWator

class World:
    def __init__(self, config: ConfigurationWator) -> None:
        self.config: ConfigurationWator = config
        self.grid_height: int = config.grid_height
        self.grid_width: int = config.grid_width
        self.grid_size: int = config.grid_height * config.grid_width
        self.grid = self.init_grid()
        self.chronons: int = 0
        self.tunas: list[Tuna] = []
        self.sharks: list[Shark] = []
        self.megalodons: list[Megalodon] = []
        
    def init_grid(self) -> list[list[Fish | None]]:
        # We use _ here because we won't use this variable for anything else in the entire code
        return [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
    
    def new_entity(self, entity: Fish):
        if not self.is_position_valid(x=entity.pos_x, y=entity.pos_y):
            return None
        if len(self.tunas) >= (self.grid_width * self.grid_height):
            return None
        
        if isinstance(entity, Megalodon):
            self.megalodons.append(entity)
        elif isinstance(entity, Shark):
            self.sharks.append(entity)
        elif isinstance(entity, Tuna):
            self.tunas.append(entity)
        
        self.grid[entity.pos_y][entity.pos_x] = entity
        
    def is_position_valid(self, x: int, y: int) -> bool:
        if x >= self.grid_width or y >= self.grid_height:
            return False
        else:
            if self.grid[y][x] == None:
                return True
            else:
                return False    
    
    def randomly_place_fishes(self, nb_sharks: int, nb_tunas: int, nb_megalodons: int):
        
        for _ in range(nb_megalodons):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
              
                if self.is_position_valid(x=x,y=y):
                    megalodon = Megalodon(x, y, self.config)
                    self.new_entity(megalodon)
                    break
        
        for _ in range(nb_sharks):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
              
                if self.is_position_valid(x=x,y=y):
                    shark = Shark(x, y, self.config)
                    self.new_entity(shark)
                    break
                
        for _ in range(nb_tunas):
            while True:
                x = random.randrange(self.grid_width)
                y = random.randrange(self.grid_height)
                
                if self.is_position_valid(x=x, y=y):
                    tuna = Tuna(x, y, self.config)
                    self.new_entity(tuna)
                    break
                
    def _process_entity(self, entity: Fish, new_entities: list):
        old_x = entity.pos_x
        old_y = entity.pos_y
        new_pos = entity.move(self.grid)
        
        self.grid[old_y][old_x] = None
        self.grid[new_pos[1]][new_pos[0]] = entity
        
        baby_fish = entity.reproduce(pos_x= old_x, pos_y= old_y)
        if baby_fish and self.is_position_valid(x= baby_fish.pos_x, y= baby_fish.pos_y):
            self.grid[baby_fish.pos_y][baby_fish.pos_x] = baby_fish
            new_entities.append(baby_fish)
    
    def world_cycle(self):
        new_megalodons: list[Megalodon] = []
        new_sharks: list[Shark] = []
        new_tunas: list[Tuna] = []
        
        for megalodon in self.megalodons:
            if megalodon.is_alive:
                self._process_entity(megalodon, new_megalodons)
                
        self.megalodons = [m for m in self.megalodons if m.is_alive]
    
        for shark in self.sharks:
            if shark.is_alive:
                self._process_entity(shark, new_sharks)

        self.sharks = [s for s in self.sharks if s.is_alive]
        
        for tuna in self.tunas:
            if tuna.is_alive:
                self._process_entity(tuna, new_tunas)
                
        self.tunas = [t for t in self.tunas if t.is_alive]
        
        self.megalodons.extend(new_megalodons)
        self.sharks.extend(new_sharks)
        self.tunas.extend(new_tunas)
        
        self.chronons += 1

