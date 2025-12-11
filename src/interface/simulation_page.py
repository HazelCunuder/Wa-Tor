import tkinter as tk
from entities.tuna import Tuna
from entities.shark import Shark
from entities.megalodon import Megalodon

class SimulationPage(tk.Frame):


    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.cell_size = 10

        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.pack(fill="both", expand=True)
        self.next_button = tk.Button(self, text="Next step", command=self.next_step)
        self.next_button.pack(pady=10)
        self.reset_button = tk.Button(self, text="Reset", command=self.reset_simulation)
        self.reset_button.pack(pady=10)
        self.draw_grid()
    def draw_grid(self):
        self.canvas.delete("all")
        world = self.controller.world

        for y in range(world.grid_height):
            for x in range(world.grid_width):

                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                entity = world.grid[y][x]
                
                if entity is None:
                    color = "black"
                elif isinstance(entity, Tuna):
                    color = "blue"
                elif isinstance(entity, Shark):
                    color = "red"
                elif isinstance(entity, Megalodon):
                    color = "purple"
                else:
                    color = "black"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def next_step(self):
        self.controller.world.world_cycle()
        self.draw_grid()

    def reset_simulation(self):
        self.controller.create_world()
        self.draw_grid()

