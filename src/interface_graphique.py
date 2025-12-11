from world import World
from simulation import Simulation
from utils.configuration import ConfigurationWator
from interface.simulation_page import SimulationPage
import tkinter as tk

class InterfaceGraphique(tk.Tk): 
    def __init__(self) -> None:
        super().__init__()
        self.title("Wa-Tor")
        self.config_wator = ConfigurationWator.__new__(ConfigurationWator)

        self.config_wator.grid_width = 50
        self.config_wator.grid_height = 50
        self.config_wator.nb_tuna = 500
        self.config_wator.nb_shark = 125
        self.config_wator.nb_megalodon = 1
        self.config_wator.time_breed_tuna = 4
        self.config_wator.times_breed_shark = 13
        self.config_wator.energy_shark = 3
        self.config_wator.recovery_energy_shark = 2
        self.config_wator.times_breed_megalodon = 10
        self.config_wator.energy_megalodon = 5
        self.config_wator.recovery_energy_megalodon = 1
        self.create_world()
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        self.page = SimulationPage(parent=container, controller=self)
        self.page.pack(fill="both", expand=True)

    def create_world(self) -> None:
        self.world = World(self.config_wator)
        self.world.randomly_place_fishes(nb_sharks = self.config_wator.nb_shark, nb_tunas = self.config_wator.nb_tuna, nb_megalodons = self.config_wator.nb_megalodon)
        self.simulation = Simulation(self.world)