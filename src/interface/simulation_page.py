import tkinter as tk
from tkinter import font
from entities.tuna import Tuna
from entities.shark import Shark
from entities.megalodon import Megalodon


class SimulationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#05668D")
        self.controller = controller
        self.cell_size = 10
        self.is_running = False
        self.after_id = None
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(1, weight=1)

        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(
            self,
            text="🪼Wa-Tor Simulation",
            font=title_font,
            bg="#05668D",
            fg="white"
        )
        title.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.canvas = tk.Canvas(self, bg="#05668D", highlightthickness=0)
        self.canvas.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=20)
        self.canvas.bind("<Configure>", self.resize_simulation)

        widget_frame = tk.Frame(self, bg="#217CA0", padx=30, pady=30)
        widget_frame.grid(row=1, column=1, padx=(10, 20), pady=20, sticky="n")

        self.parametrage_button = tk.Button(
            widget_frame,
            text="⚙ Settings",
            command=lambda: self.controller.show_page("SettingPage"),
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=5,
        )
        self.parametrage_button.pack(pady=(0, 10), fill="x")

        self.next_step_button = tk.Button(
            widget_frame,
            text="▶ Next Step",
            command=self.next_step,
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=5,
        )
        self.next_step_button.pack(pady=5, fill="x")

        self.run_simulation_button = tk.Button( 
            widget_frame,
            text="▶ Start",
            command=self.run_simulation,
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=5,
        )
        self.run_simulation_button.pack(pady=5, fill="x")

        self.reset_button = tk.Button(
            widget_frame,
            text="🔄 Reset",
            command=self.reset_simulation,
            bg="#217CA0",
            fg="#f5e0dc",
            activebackground="#05668D",
            activeforeground="#f5e0dc",
            relief="raised",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=5,
        )
        self.reset_button.pack(pady=5, fill="x")

        self.info_simulation = tk.Label(
            widget_frame,
            text="",
            bg="#217CA0",
            fg="#cdd6f4",
            justify="left",
            anchor="w",
            font=("Arial", 10)
        )
        self.info_simulation.pack(pady=10, fill="x")

        self.draw_grid()

    def draw_grid(self):
        self.canvas.delete("all")
        world = self.controller.world

        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        offset_x = (canvas_w - (canvas_w * 0.85)) / 2
        offset_y = (canvas_h - (canvas_h * 0.85)) / 2
        cell_w = (canvas_w * 0.85) / world.grid_width
        cell_h = (canvas_h * 0.85) / world.grid_height

        for y in range(world.grid_height):
            for x in range(world.grid_width):
                x1 = offset_x + x * cell_w
                x2 = x1 + cell_w
                y1 = offset_y + y * cell_h
                y2 = y1 + cell_h

                entity = world.grid[y][x]
                emoji = ""
                bg_color = "#217CA0"
                if isinstance(entity, Tuna) and entity.is_alive:
                    bg_color = "#05668D"
                    emoji = "🐟"
                elif isinstance(entity, Shark) and entity.is_alive:
                    bg_color = "#FF4D4D"
                    emoji = "🦈"
                elif isinstance(entity, Megalodon) and entity.is_alive:
                    bg_color = "#32CD32"
                    emoji = "🐋"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=bg_color, outline=bg_color)

                if emoji:
                    self.canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text=emoji,
                        font=("Arial", int(min(cell_w, cell_h) * 0.8))
                    )

        self.update_info(world)

    def update_info(self, world):
        self.info_simulation.config(
            text=(
                f"Chronon  : {world.chronons}\n"
                f"Tunas    : {len(world.tunas)}\n"
                f"Sharks   : {len(world.sharks)}\n"
                f"Megalodons : {len(world.megalodons)}"
            )
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
        self.stop_auto_run()
        self.draw_grid()

    def run_simulation(self):
        self.is_running = not self.is_running

        if self.is_running:
            self.run_simulation_button.config(text="⏸ Stop")
            self.auto_run()
        else:
            self.stop_auto_run()

    def auto_run(self):
        if not self.is_running:
            return
        elif (
            len(self.controller.world.tunas) == 0
            or len(self.controller.world.sharks) == 0 or len(self.controller.world.megalodons) == 0
        ):
            self.stop_auto_run()

            if self.controller.world.chronons % 10 != 0:
                self.controller.simulation.chronon_history.append((
                    self.controller.world.chronons,
                    len(self.controller.world.tunas),
                    len(self.controller.world.sharks),
                    len(self.controller.world.megalodons)
                ))

            sim_id = self.controller.simulation.save.save_sim_data(self.controller.simulation.get_results())
            self.controller.simulation.save.save_chronon_data(sim_id, self.controller.simulation.chronon_history)           
            return
        else:
            self.controller.world.world_cycle()
            self.controller.simulation.graph.update(
                self.controller.world.chronons,
                len(self.controller.world.tunas),
                len(self.controller.world.sharks),
                len(self.controller.world.megalodons)
            )

            if self.controller.world.chronons % 10 == 0:
                self.controller.simulation.chronon_history.append((
                    self.controller.world.chronons,
                    len(self.controller.world.tunas),
                    len(self.controller.world.sharks),
                    len(self.controller.world.megalodons)
                ))  
                
            self.draw_grid()
            self.after_id = self.after(200, self.auto_run)

    def stop_auto_run(self):
        self.is_running = False
        self.run_simulation_button.config(text="▶ Start")

        if self.after_id is not None:
            try:
                self.after_cancel(self.after_id)
            except:
                pass
            self.after_id = None

    def resize_simulation(self, event):
        self.canvas_width = event.width
        self.canvas_height = event.height
        self.draw_grid()