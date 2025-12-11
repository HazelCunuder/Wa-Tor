from entities.fish import Fish
from world import World
from utils.data_manager import DataManager
from simulation_graph import SimulationGraph
import datetime

class Simulation:
    def __init__(self, world: World, graph: SimulationGraph):
        """
        Initialize the simulation with a world and setup data tracking.
        Creates a DataManager instance for saving results and initializes an empty list to track population history over time.
        
        Parameters:
            world (World): The world instance containing the ecosystem grid and entities
        """
        self.world = world
        self.save = DataManager()
        self.chronon_history: list = []
        self.graph = graph
    
    def display_grid(self) -> list[list[str]]:
        """
        Create a 2D representation of the world grid with entity emojis.
        Returns a grid structure instead of printing directly to allow better visualization formatting in the console through print_grid_ascii().
        Fish entities are represented by their emoji property and empty cells are represented by spaces.
        
        Returns:
            list[list[str]]: 2D list representing the visual state of the world, where each cell contains either a fish emoji or a space
        """
        display = [[" " for _ in range(self.world.grid_width)] for _ in range(self.world.grid_height)]
        
        for y in range(len(self.world.grid)):
            for x in range(len(self.world.grid[0])):
                cell = self.world.grid[y][x]
                if isinstance(cell, Fish):
                    display[y][x] = cell.emoji
                else:
                    display[y][x] = " "
        return display

    def run_simulation(self, world: World, graph: SimulationGraph):
        """
        Run the Wa-Tor simulation with real-time graph visualization.
        
        Initializes the simulation, displays the initial state, and starts
        the step-by-step simulation loop with graph updates.
        
        Args:
            world (World): The world object containing the grid and entities
            graph (SimulationGraph): The graph object for visualization
        """
        self.world = world
        self.graph = graph
        
        print("Initial state: ")
        self.print_grid_ascii()
        
        self._simulation_step()
        
        self.graph.show()

    def _simulation_step(self):
        """
        Execute one chronon of the simulation.
        
        Performs one world cycle, updates the display, records population data,
        updates the graph, and schedules the next step. If the simulation is over,
        saves data to the database and stops.
        """
        if not self.is_simulation_over():
            print("\n")
            self.world.world_cycle()
            self.print_grid_ascii()
            
            if self.world.chronons % 10 == 0:
                self.chronon_history.append((
                    self.world.chronons,
                    len(self.world.tunas),
                    len(self.world.sharks),
                    len(self.world.megalodons)
                ))
            
            self.graph.update(
                self.world.chronons,
                len(self.world.tunas),
                len(self.world.sharks),
                len(self.world.megalodons)
            )
            
            print(f"Number of sharks left: {len(self.world.sharks)}")
            print(f"Number of tunas left: {len(self.world.tunas)}")
            print(f"Total Chronons: {self.world.chronons}")
            
            self.graph.root.after(100, self._simulation_step)
        else:
            if self.world.chronons % 10 != 0:
                self.chronon_history.append((
                    self.world.chronons,
                    len(self.world.tunas),
                    len(self.world.sharks),
                    len(self.world.megalodons)
                ))
            
            sim_id = self.save.save_sim_data(self.get_results())
            self.save.save_chronon_data(sim_id, self.chronon_history) 
        
    def print_grid_ascii(self):
        """
        Print the current world grid to console with ASCII borders.
        Creates a bordered table representation of the grid for clear terminal visualization of the ecosystem state.
        Uses the display_grid() method to get the grid data and formats it with borders for readability.
        """
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
        """
        Check if simulation termination conditions have been met.
        Ends the simulation when any species reaches zero population, as the goal is to find parameters that allow all three species to reach equilibrium and coexist.
        
        Returns:
            bool: True if any species population (tunas, sharks, or megalodons) has reached zero, False otherwise
        """
        return len(self.world.tunas) == 0 or len(self.world.sharks) == 0 or len(self.world.megalodons) == 0
    
    def get_results(self) -> dict:
        """
        Compile simulation results into a dictionary for storage.
        Captures timestamp components separately (date, hours, minutes) to allow multiple simulations to be distinguished when run within the same hour, along with grid dimensions and final chronon count.
        This dictionary structure matches the schema expected by the DataManager's save_sim_data() method.
        
        Returns:
            dict: Dictionary containing simulation metadata and results with keys:
                - 'experiment_date' (datetime.date): Date when the simulation was run
                - 'hours' (int): Hour component of when the simulation completed
                - 'minutes' (int): Minute component of when the simulation completed
                - 'grid_height' (int): Height of the simulation grid
                - 'grid_width' (int): Width of the simulation grid
                - 'chronons_reached' (int): Total number of time steps completed before termination
        """
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