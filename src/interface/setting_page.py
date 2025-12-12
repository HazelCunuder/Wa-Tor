import tkinter as tk
from tkinter import font
from utils.configuration import ConfigurationWator


class SettingPage(tk.Frame):
    def __init__(self, parent : object, controller : object) -> None:
        super().__init__(parent, bg="#05668D")
        self.controller = controller

        title_font = font.Font(family="Helvetica", size=24, weight="bold")
        title = tk.Label(
            self,
            text="🪼Wa-Tor Simulation",
            font=title_font,
            bg="#05668D",
            fg="white"
        )
        title.pack(pady=20)

        subtitle = tk.Label(
            self,
            text="Simulation Configuration 🛠️",
            font=("Arial", 12),
            bg="#05668D",
            fg="#cdd6f4"
        )
        subtitle.pack()

        frame = tk.Frame(self, bg="#217CA0", padx=50, pady=50)
        frame.pack(pady=30)


        tk.Label(frame, text="Enter the grid's width:", bg="#217CA0", fg="#f5e0dc").grid(row=0, column=0, sticky="w", pady=5)
        self.entry_width = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_width.insert(0, "50")
        self.entry_width.grid(row=0, column=1, padx=10)

        tk.Label(frame, text="Enter the grid's height: ", bg="#217CA0", fg="#f5e0dc").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_height = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_height.insert(0, "50")
        self.entry_height.grid(row=1, column=1, padx=10)

        tk.Label(frame, text="Enter the number of tunas in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_tuna = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_tuna.insert(0, "500")
        self.entry_tuna.grid(row=2, column=1, padx=10)

        tk.Label(frame, text="Enter the number of sharks in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=3, column=0, sticky="w", pady=5)
        self.entry_shark = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_shark.insert(0, "125")
        self.entry_shark.grid(row=3, column=1, padx=10)

        tk.Label(frame, text="Enter the number of megalodons in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=4, column=0, sticky="w", pady=5)
        self.entry_mega = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_mega.insert(0, "20")
        self.entry_mega.grid(row=4, column=1, padx=10)

        tk.Label(frame, text="Choose the breed cooldown for tunas: ", bg="#217CA0", fg="#f5e0dc").grid(row=5, column=0, sticky="w", pady=5)
        self.entry_breed_tuna = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_breed_tuna.insert(0, "4")
        self.entry_breed_tuna.grid(row=5, column=1, padx=10)

        tk.Label(frame, text="Choose the breed cooldown for sharks: ", bg="#217CA0", fg="#f5e0dc").grid(row=6, column=0, sticky="w", pady=5)
        self.entry_breed_shark = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_breed_shark.insert(0, "13")
        self.entry_breed_shark.grid(row=6, column=1, padx=10)

        tk.Label(frame, text="Choose the breed cooldown for megalodons: ", bg="#217CA0", fg="#f5e0dc").grid(row=7, column=0, sticky="w", pady=5)
        self.entry_breed_mega = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_breed_mega.insert(0, "20")
        self.entry_breed_mega.grid(row=7, column=1, padx=10)

        tk.Label(frame, text="Enter the initial energy for the sharks: ", bg="#217CA0", fg="#f5e0dc").grid(row=8, column=0, sticky="w", pady=5)
        self.entry_energy_shark = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_energy_shark.insert(0, "3")
        self.entry_energy_shark.grid(row=8, column=1, padx=10)

        tk.Label(frame, text="Enter the initial energy for the megalodons: ", bg="#217CA0", fg="#f5e0dc").grid(row=9, column=0, sticky="w", pady=5)
        self.entry_energy_mega = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_energy_mega.insert(0, "3")
        self.entry_energy_mega.grid(row=9, column=1, padx=10)

        tk.Label(frame, text="Enter the energy sharks gain when eating a tuna: ", bg="#217CA0", fg="#f5e0dc").grid(row=10, column=0, sticky="w", pady=5)
        self.entry_rec_shark = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_rec_shark.insert(0, "2")
        self.entry_rec_shark.grid(row=10, column=1, padx=10)

        tk.Label(frame, text="Enter the energy megalodons gain when eating a tuna: ", bg="#217CA0", fg="#f5e0dc").grid(row=11, column=0, sticky="w", pady=5)
        self.entry_rec_mega = tk.Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
        self.entry_rec_mega.insert(0, "1")
        self.entry_rec_mega.grid(row=11, column=1, padx=10)

        button_frame = tk.Frame(self, bg="#05668D")
        button_frame.pack(pady=20)

        apply_button = tk.Button(
            button_frame,
            text="✅ Apply and return",
            command=self.apply_and_back,
            bg="#217CA0",
            fg="#f5e0dc",
            font=("Arial", 12, "bold"),
            padx=20,
            pady=5,
        )
        apply_button.pack(side="left", padx=10)

    def apply_and_back(self) -> None:
        config = self.controller.config_wator

        config.grid_width = int(self.entry_width.get())
        config.grid_height = int(self.entry_height.get())
        config.nb_tuna = int(self.entry_tuna.get())
        config.nb_shark = int(self.entry_shark.get())
        config.nb_megalodon = int(self.entry_mega.get())

        config.time_breed_tuna = int(self.entry_breed_tuna.get())
        config.times_breed_shark = int(self.entry_breed_shark.get())
        config.times_breed_megalodon = int(self.entry_breed_mega.get())
        config.energy_shark = int(self.entry_energy_shark.get())
        config.energy_megalodon = int(self.entry_energy_mega.get())
        config.recovery_energy_shark = int(self.entry_rec_shark.get())
        config.recovery_energy_megalodon = int(self.entry_rec_mega.get())
        self.controller.create_world()
        self.controller.pages["SimulationPage"].draw_grid()
        self.controller.show_page("SimulationPage")
