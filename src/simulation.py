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
    
    def run_simulation(self):
        new_sharks: list[Shark] = []
        new_tunas: list[Tuna] = []    
    
    
        for shark in self.world.sharks:
            if shark and shark.is_alive:
                old_x = shark.pos_x
                old_y = shark.pos_y
                new_pos = shark.move(self.world.grid)
                self.world.grid[old_y][old_x] = None
                self.world.grid[new_pos[1]][new_pos[0]] = shark
                baby_shark = shark.reproduce(pos_x= old_x, pos_y= old_y)
                if baby_shark and self.world.is_position_valid(x= baby_shark.pos_x, y= baby_shark.pos_y):
                    self.world.grid[baby_shark.pos_y][baby_shark.pos_x] = baby_shark
                    new_sharks.append(baby_shark)
            if shark and not shark.is_alive:
                old_x = shark.pos_x
                old_y = shark.pos_y
                self.world.grid[old_y][old_x] = None
                self.world.sharks.remove(shark)
                self.world.fishes.remove(shark)

        for tuna in self.world.tunas:
            if tuna and tuna.is_alive:
                old_x = tuna.pos_x
                old_y = tuna.pos_y
                new_pos = tuna.move(self.world.grid)
                self.world.grid[old_y][old_x] = None
                self.world.grid[new_pos[1]][new_pos[0]] = tuna
                baby_tuna = tuna.reproduce(pos_x = old_x, pos_y = old_y)
                if baby_tuna and self.world.is_position_valid(x = baby_tuna.pos_x, y = baby_tuna.pos_y):
                    self.world.grid[baby_tuna.pos_y][baby_tuna.pos_x] = baby_tuna
                    new_tunas.append(baby_tuna)
            if tuna and not tuna.is_alive:
                old_x = tuna.pos_x
                old_y = tuna.pos_y
                self.world.grid[old_y][old_x] = None
                self.world.tunas.remove(tuna)
                self.world.fishes.remove(tuna)

        self.world.sharks.extend(new_sharks)
        self.world.tunas.extend(new_tunas)
        
        self.world.fishes.extend(new_sharks)
        self.world.fishes.extend(new_tunas)
        
        self.world.chronons += 1
        
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