from entities.tuna import Tuna
from entities.shark import Shark
from world import World

class Simulation:
    def __init__(self, world: World):
        self.world = world
    
    def display_grid(self) -> list[list[str]]:
        display = [[" " for _ in range(self.world.grid_width)] for _ in range(self.world.grid_height)]
        
        for y in range(len(self.world.grid)):
            for x in range(len(self.world.grid[0])):
                cell = self.world.grid[y][x]
                if isinstance(cell, Shark):
                    display[y][x] = cell.emoji_shark
                elif isinstance(cell, Tuna):
                    display[y][x] = cell.emoji_tuna
                else:
                    display[y][x] = " "
        return display
    
    def run_simulation(self, world: World):
        print("Initial state: ")
        self.print_grid_ascii()
        
        while not self.is_simulation_over():
            print("\n")
            world.world_cycle()
            self.print_grid_ascii()
            
        print(f"Number of sharks left: {len(world.sharks)}")
        print(f"Number of tunas left: {len(world.tunas)}")
        print(f"Total Chronons: {world.chronons}")
        
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
            
    def is_simulation_over(self) -> bool:
        total_fish: int = len(self.world.fishes)
        
        if total_fish == 0:
            return True
        
        total_cells: int = self.world.grid_size
        if total_fish >= total_cells:
            return True
        
        return False
    
    def get_results(self) -> dict:
        results = {
            "grid_height": self.world.grid_height,
            "grid_width": self.world.grid_width,
            "chronons_reached": self.world.chronons,
            "tunas_left": len(self.world.tunas),
            "sharks_left": len(self.world.sharks)
        }
        
        return results