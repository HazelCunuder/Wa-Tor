from world import World
from simulation import Simulation
from entities import *
from utils.configuration import ConfigurationWator

config = ConfigurationWator()

planet: World = World(config)

planet.randomly_place_fishes(nb_sharks = config.nb_shark, nb_tunas = config.nb_tuna, nb_megalodons=1)

sim = Simulation(planet)

sim.run_simulation(planet)