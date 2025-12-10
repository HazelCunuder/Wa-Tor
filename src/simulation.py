from entities.fish import Fish
from world import World
from utils.data_manager import DataManager
import datetime

class Simulation:
    def __init__(self, world: World):
        self.world = world
        self.save = DataManager()
        self.chronon_history: list = []
    
    def display_grid(self) -> list[list[str]]:
        display = [[" " for _ in range(self.world.grid_width)] for _ in range(self.world.grid_height)]
        
        for y in range(len(self.world.grid)):
            for x in range(len(self.world.grid[0])):
                cell = self.world.grid[y][x]
                if isinstance(cell, Fish):
                    display[y][x] = cell.emoji
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
            
            if self.world.chronons % 10 == 0:
                self.chronon_history.append((world.chronons, len(world.tunas), len(world.sharks), len(world.megalodons)))
                
        if self.world.chronons % 10 != 0:
            self.chronon_history.append((world.chronons,len(world.tunas), len(world.sharks), len(world.megalodons)))
          
        print(f"Number of sharks left: {len(world.sharks)}")
        print(f"Number of tunas left: {len(world.tunas)}")
        print(f"Total Chronons: {world.chronons}")
        
        sim_id = self.save.save_sim_data(self.get_results())
        self.save.save_chronon_data(sim_id, self.chronon_history)
        
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
        total_tunas: int = len(self.world.tunas)
        total_sharks: int = len(self.world.sharks)
        
        if total_tunas == 0:
            return True
        
        if total_sharks == 0:
            return True
        
        return False
    
    def get_results(self) -> dict:
        now = datetime.datetime.now()
        
        results = {
            "experiment_date": now.date(),
            "hours": now.hour,
            "minutes": now.minute,
            "grid_height": self.world.grid_height,
            "grid_width": self.world.grid_width,
            "chronons_reached": self.world.chronons,
        }
        
        return results