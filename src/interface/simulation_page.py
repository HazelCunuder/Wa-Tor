import tkinter as tk
from entities.tuna import Tuna
from entities.shark import Shark
from entities.megalodon import Megalodon

class SimulationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.cell_size = 10
        self.is_running = False

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self, bg="black")
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.canvas.bind("<Configure>", self.resize_simulation)

        widget_frame = tk.Frame(self)
        widget_frame.grid(row=0, column=1, padx=50)
        
        self.parametrage_button = tk.Button(
                widget_frame,
                text="Settings",
                command=lambda: self.controller.show_page("SettingPage"),
                bg="#217CA0",
                fg="#f5e0dc",
                activebackground="#05668D",
                activeforeground="#f5e0dc",
                relief="raised"
            )
        self.parametrage_button.pack(pady=10, fill="x")
        
        self.run_simulation_button = tk.Button(
            widget_frame,
            text="Start",
            command=self.run_simulation,
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised"
        )
        self.run_simulation_button.pack(pady=5, fill="x")

        self.reset_button = tk.Button(
            widget_frame,
            text="Reset",
            command=self.reset_simulation,
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised"
        )
        self.reset_button.pack(pady=5, fill="x")

        self.info_simulation = tk.Label(
            widget_frame,
            text="",
            bg="#217CA0",
            fg="#cdd6f4",
            justify="left"
        )
        self.info_simulation.pack(pady=10, anchor="w")

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        world = self.controller.world

        for y in range(world.grid_height):
            for x in range( world.grid_width):

                x1 = x * (self.canvas.winfo_width() / world.grid_width)
                x2 = x1 + (self.canvas.winfo_width() / world.grid_width)
                y1 = y * (self.canvas.winfo_height() / world.grid_height)
                y2 = y1 + (self.canvas.winfo_height() / world.grid_height)

                entity = world.grid[y][x]


                if entity is None:
                    color = "black"
                elif isinstance(entity, Tuna) and entity.is_alive:
                    color = "blue"
                elif isinstance(entity, Shark) and entity.is_alive:
                    color = "red"
                elif isinstance(entity, Megalodon) and entity.is_alive:
                    color = "purple"
                else:
                    color = "black"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        
        self.update_info(world)

    def update_info(self, world):
        self.info_simulation.config(
            text=f"Chronon : {world.chronons}\n"
             f"Tunas : {len(world.tunas)}\n"
             f"Sharks : {len(world.sharks)}\n"
             f"Megalodons : {len(world.megalodons)}"
        )
    
    def next_step(self):
        self.controller.world.world_cycle()
        self.controller.simulation.graph.update(
            self.controller.world.chronons,
            len(self.controller.world.tunas),
            len(self.controller.world.sharks),
            len(self.controller.world.megalodons)
        )
        self.draw_grid()

    def reset_simulation(self):
        self.controller.create_world()
        self.is_running = False
        self.run_simulation_button.config(text="Start")
        self.draw_grid()

    def run_simulation(self):
        self.is_running = not self.is_running

        if self.is_running:
            self.run_simulation_button.config(text="Stop")
            self.auto_run()
        else:
            self.run_simulation_button.config(text="Start")

    def auto_run(self):
        if not self.is_running:
            return
        self.controller.world.world_cycle()
        self.controller.simulation.graph.update(
            self.controller.world.chronons,
            len(self.controller.world.tunas),
            len(self.controller.world.sharks),
            len(self.controller.world.megalodons)
        )

        self.draw_grid()
        self.after(200, self.auto_run)

    def resize_simulation(self, event):
        self.canvas_width = event.width
        self.canvas_height = event.height
        self.draw_grid()