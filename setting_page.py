import os
import sys

# --- FIX PATH & MACOS ---
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, "src")
sys.path.append(src_dir)

tcl_library = "/usr/local/opt/tcl-tk/lib"
if os.path.exists(tcl_library):
    os.environ["TCL_LIBRARY"] = os.path.join(tcl_library, "tcl8.6")
    os.environ["TK_LIBRARY"] = os.path.join(tcl_library, "tk8.6")

print("🖥️ Starting GUI...")

from tkinter import *
from tkinter import font

from utils.configuration import ConfigurationWator
from world import World
from simulation import Simulation


window = Tk()
window.title("Wa-Tor - Configuration")
window.geometry("500x600")
window.configure(bg="#05668D")


title_font = font.Font(family="Helvetica", size=24, weight="bold")
title = Label(
    window,
    text="🪼Wa-Tor Simulation",
    font=title_font,
    bg="#05668D",
    fg="white"
)
title.pack(pady=20)

subtitle = Label(
    window,
    text="Simulation Configuration 🛠️",
    font=("Arial", 12),
    bg="#05668D",
    fg="#cdd6f4"
)
subtitle.pack()

frame = Frame(window, bg="#217CA0", padx=50, pady=50)
frame.pack(pady=30)

# --- INPUTS ---
Label(frame, text="Enter the grid's width: ", bg="#217CA0", fg="#f5e0dc").grid(row=0, column=0, sticky="w", pady=5)
entry_width = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_width.insert(0, "10")
entry_width.grid(row=0, column=1, padx=10)

Label(frame, text="Enter the grid's height: ", bg="#217CA0", fg="#f5e0dc").grid(row=1, column=0, sticky="w", pady=5)
entry_height = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_height.insert(0, "10")
entry_height.grid(row=1, column=1, padx=10)

Label(frame, text="Enter the number of tunas in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=2, column=0, sticky="w", pady=5)
entry_tuna = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_tuna.insert(0, "25")
entry_tuna.grid(row=2, column=1, padx=10)

Label(frame, text="Enter the number of sharks in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=3, column=0, sticky="w", pady=5)
entry_shark = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_shark.insert(0, "5")
entry_shark.grid(row=3, column=1, padx=10)

Label(frame, text="Enter the number of megalodons in the world: ", bg="#217CA0", fg="#f5e0dc").grid(row=4, column=0, sticky="w", pady=5)
entry_mega = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_mega.insert(0, "1")
entry_mega.grid(row=4, column=1, padx=10)

Label(frame, text="Choose the breed cooldown for tunas: ", bg="#217CA0", fg="#f5e0dc").grid(row=5, column=0, sticky="w", pady=5)
entry_breed_tuna = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_breed_tuna.insert(0, "3")
entry_breed_tuna.grid(row=5, column=1, padx=10)

Label(frame, text="Choose the breed cooldown for sharks: ", bg="#217CA0", fg="#f5e0dc").grid(row=6, column=0, sticky="w", pady=5)
entry_breed_shark = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_breed_shark.insert(0, "5")
entry_breed_shark.grid(row=6, column=1, padx=10)

Label(frame, text="Choose the breed cooldown for megalodons: ", bg="#217CA0", fg="#f5e0dc").grid(row=7, column=0, sticky="w", pady=5)
entry_breed_mega = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_breed_mega.insert(0, "10")
entry_breed_mega.grid(row=7, column=1, padx=10)

Label(frame, text="Enter the initial energy for the sharks: ", bg="#217CA0", fg="#f5e0dc").grid(row=8, column=0, sticky="w", pady=5)
entry_energy_shark = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_energy_shark.insert(0, "3")
entry_energy_shark.grid(row=8, column=1, padx=10)

Label(frame, text="Enter the initial energy for the megalodons: ", bg="#217CA0", fg="#f5e0dc").grid(row=9, column=0, sticky="w", pady=5)
entry_energy_mega = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_energy_mega.insert(0, "3")
entry_energy_mega.grid(row=9, column=1, padx=10)

Label(frame, text="Enter the energy sharks gain when eating a tuna: ", bg="#217CA0", fg="#f5e0dc").grid(row=10, column=0, sticky="w", pady=5)
entry_rec_shark = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_rec_shark.insert(0, "2")
entry_rec_shark.grid(row=10, column=1, padx=10)

Label(frame, text="Enter the energy megalodons gain when eating a tuna: ", bg="#217CA0", fg="#f5e0dc").grid(row=11, column=0, sticky="w", pady=5)
entry_rec_mega = Entry(frame, width=5, bg="#217CA0", fg="#f5e0dc", justify="center")
entry_rec_mega.insert(0, "1")
entry_rec_mega.grid(row=11, column=1, padx=10)


def start_simulation():
    try:
        config = ConfigurationWator(interactive=False)

        config.grid_width = int(entry_width.get())
        config.grid_height = int(entry_height.get())
        config.nb_tuna = int(entry_tuna.get())
        config.nb_shark = int(entry_shark.get())
        config.nb_megalodon = int(entry_mega.get())

        config.time_breed_tuna = int(entry_breed_tuna.get())
        config.times_breed_shark = int(entry_breed_shark.get())
        config.times_breed_megalodon = int(entry_breed_mega.get())
        config.energy_shark = int(entry_energy_shark.get())
        config.recovery_energy_shark = int(entry_rec_shark.get())
        config.energy_megalodon = int(entry_energy_mega.get())
        config.recovery_energy_megalodon = int(entry_rec_mega.get())

        print("✅ Configuration loaded!")

        planet = World(config)
        planet.randomly_place_fishes(
            nb_sharks=config.nb_shark,
            nb_tunas=config.nb_tuna,
            nb_megalodons=config.nb_megalodon
        )

        sim = Simulation(planet)
        sim.run_simulation(planet)

    except ValueError:
        print("❌ Error: Please enter valid numbers!")


button = Button(
    window,
    text="🌊 Let's start",
    command=start_simulation,
    bg="#217CA0",
    fg="#05668D",
    font=("Arial", 12, "bold"),
    padx=20,
    pady=5,
    relief="raised",
    cursor="hand2"
)
button.pack(pady=20)
window.mainloop()
