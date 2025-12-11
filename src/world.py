import random
from entities.fish import Fish
from entities.tuna import Tuna
from entities.shark import Shark
from entities.megalodon import Megalodon
from utils.configuration import ConfigurationWator

class World:
    def __init__(self, config: ConfigurationWator) -> None:
        """
        Initialize the world with a configuration and setup the ecosystem grid.
        Creates an empty grid based on configuration dimensions and initializes empty lists to track each species population.
        The chronon counter starts at 0 to track simulation time steps.
        
        Parameters:
            config (ConfigurationWator): Configuration object containing grid dimensions and entity parameters
        """
        
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
        """
        Create an empty 2D grid to represent the world space.
        Initializes all cells to None to represent empty water where fish can be placed.
        We use _ for the loop variable because it's not referenced within the loop as per .
        
        Returns:
            list[list[Fish | None]]: 2D grid with dimensions grid_height x grid_width, all cells initialized to None
        """
        
        return [[None for _ in range(self.grid_width)] for _ in range(self.grid_height)]
    
    def new_entity(self, entity: Fish):
        """
        Add a new fish entity to the world at its specified position.
        Validates the position before placement and adds the entity to the appropriate species list.
        We check grid capacity to prevent overpopulation and separate entities by type for efficient processing during world cycles.
        
        Parameters:
            entity (Fish): The fish entity to add (can be Tuna, Shark, or Megalodon)
        """
        
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
        """
        Check if a grid position is within bounds and unoccupied.
        Validates that coordinates don't exceed grid dimensions and that the target cell is empty (None).
        This prevents entities from overlapping or moving outside the world boundaries.
        
        Parameters:
            x (int): X coordinate to validate
            y (int): Y coordinate to validate
            
        Returns:
            bool: True if position is within grid bounds and the cell is empty, False otherwise
        """
        
        if x >= self.grid_width or y >= self.grid_height:
            return False
        else:
            if self.grid[y][x] == None:
                return True
            else:
                return False    
    
    def randomly_place_fishes(self, nb_sharks: int, nb_tunas: int, nb_megalodons: int):
        """
        Populate the world grid with initial fish populations at random valid positions.
        Places megalodons first, then sharks, then tunas to establish the initial ecosystem state.
        Uses while loops with random coordinate generation to find empty cells, ensuring no overlap between entities.
        
        Parameters:
            nb_sharks (int): Number of sharks to place in the world
            nb_tunas (int): Number of tunas to place in the world
            nb_megalodons (int): Number of megalodons to place in the world
        """
    
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
        """
        Handle a single entity's turn by moving it and checking for reproduction.
        Updates the grid to reflect the entity's new position and adds any offspring to the new_entities list.
        This is a helper method called during world_cycle() to process each living entity.
        We clear the old position before setting the new one to maintain grid consistency.
        
        Parameters:
            entity (Fish): The fish entity to process
            new_entities (list): List to append newborn fish to (passed by reference to accumulate offspring)
        """
        
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
        """
        Execute one time step of the simulation for all entities.
        Processes each species in order (megalodons, sharks, tunas), moving living entities and handling reproduction.
        Removes dead entities from species lists and adds newborns after all movements are complete to avoid processing them twice in the same cycle.
        Increments the chronon counter to track total simulation time.
        We process species separately to maintain clear predator-prey hierarchy during each cycle.
        """
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

