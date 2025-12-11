from world import World
from simulation import Simulation
from entities import *
from utils.configuration import ConfigurationWator
from utils.data_manager import DataManager
from simulation_graph import SimulationGraph

config = ConfigurationWator()

data_manager = DataManager()
data_manager.create_tables()

planet: World = World(config)
planet.randomly_place_fishes(nb_sharks=config.nb_shark, nb_tunas=config.nb_tuna, nb_megalodons=config.nb_megalodon)

graph = SimulationGraph()

sim = Simulation(planet, graph)
sim.run_simulation(planet, graph)