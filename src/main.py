from world import World
from simulation import Simulation
from entities import *

input_height: int = int(input("Enter a height: "))
input_width: int = int(input("Enter a width: "))
input_tunas: int = int(input("How many tunas in the simulation? "))
input_sharks: int = int(input("How many sharks in the simulation? "))

planet: World = World(height= input_height, width=input_width)

planet.randomly_place_fishes(nb_sharks = input_sharks, nb_tunas = input_tunas)

sim = Simulation(planet)

sim.run_simulation(planet)