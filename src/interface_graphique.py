import tkinter as tk
from world import World
from simulation import Simulation

CELL_SIZE = 30 


class InterfaceGraphique:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.is_running = False  # auto-play en cours ?

        # === 1) Paramètres de départ ===
        self.height: int = 10
        self.width: int = 10
        self.nb_tunas: int = 20
        self.nb_sharks: int = 5

        # === 2) Créer le monde et la simulation ===
        self.create_world()

        # === 3) Créer l'UI ===
        self.create_widgets()

        # === 4) Premier affichage ===
        self.draw_grid()

    # --------------------------------------------------------------
    # Création du monde (utilisée aussi pour Reset)
    # --------------------------------------------------------------
    def create_world(self):
        """Crée un nouveau monde + simulation."""
        self.world = World(height=self.height, width=self.width)
        self.world.randomly_place_fishes(
            nb_sharks=self.nb_sharks,
            nb_tunas=self.nb_tunas,
        )
        self.simulation = Simulation(self.world)

        # infos dessin
        self.cell_size = CELL_SIZE
        self.grid_width = self.world.grid_width
        self.grid_height = self.world.grid_height

    # --------------------------------------------------------------
    # Création des widgets
    # --------------------------------------------------------------
    def create_widgets(self) -> None:
        main_frame = tk.Frame(self.root)
        main_frame.pack(padx=10, pady=10)

        # Canvas
        self.canvas = tk.Canvas(
            main_frame,
            width=self.grid_width * self.cell_size,
            height=self.grid_height * self.cell_size,
            bg="white",
        )
        self.canvas.grid(row=0, column=0, columnspan=4)

        # Boutons
        self.next_button = tk.Button(main_frame, text="Étape suivante", command=self.next_step)
        self.next_button.grid(row=1, column=0, padx=5, pady=5)

        self.start_pause_button = tk.Button(main_frame, text="Start auto", command=self.toggle_run)
        self.start_pause_button.grid(row=1, column=1, padx=5, pady=5)

        self.reset_button = tk.Button(main_frame, text="Reset", command=self.reset_world)
        self.reset_button.grid(row=1, column=2, padx=5, pady=5)

        self.quit_button = tk.Button(main_frame, text="Quitter", command=self.root.destroy)
        self.quit_button.grid(row=1, column=3, padx=5, pady=5)

    # --------------------------------------------------------------
    # Dessiner la grille
    # --------------------------------------------------------------
    def draw_grid(self) -> None:
        self.canvas.delete("all")
        display = self.simulation.display_grid()

        for y, row in enumerate(display):
            for x, cell in enumerate(row):
                x1 = x * self.cell_size
                y1 = y * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # case
                self.canvas.create_rectangle(x1, y1, x2, y2)

                # emoji
                if cell != " ":
                    self.canvas.create_text(
                        (x1 + x2) // 2,
                        (y1 + y2) // 2,
                        text=cell,
                        font=("Arial", 14),
                    )

    # --------------------------------------------------------------
    # Actions des boutons
    # --------------------------------------------------------------
    def next_step(self) -> None:
        self.world.world_cycle()
        self.draw_grid()

    def toggle_run(self) -> None:
        if self.is_running:
            self.is_running = False
            self.start_pause_button.config(text="Start auto")
        else:
            self.is_running = True
            self.start_pause_button.config(text="Pause")
            self.run_auto()

    def run_auto(self) -> None:
        if not self.is_running:
            return
        self.world.world_cycle()
        self.draw_grid()
        self.root.after(200, self.run_auto)

    def reset_world(self) -> None:
        """Réinitialise totalement la simulation."""
        # Arrêter l'autoplay si en cours
        self.is_running = False
        self.start_pause_button.config(text="Start auto")

        # Recréer le monde + simulation
        self.create_world()

        # Redessiner
        self.draw_grid()


def main() -> None:
    root = tk.Tk()
    root.title("Wa-Tor - Interface graphique")
    app = InterfaceGraphique(root)
    root.mainloop()


if __name__ == "__main__":
    main()
