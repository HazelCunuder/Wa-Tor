from world import World
from simulation import Simulation
from entities import *
from utils.configuration import ConfigurationWator

config = ConfigurationWator()

planet: World = World(height= config.grid_height, width=config.grid_width)

planet.randomly_place_fishes(nb_sharks = config.nb_shark, nb_tunas = config.nb_tuna)

sim = Simulation(planet)

sim.run_simulation(planet)