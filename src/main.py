from world import World
from entities import *

input_height: int = int(input("Enter a height: "))
input_width: int = int(input("Enter a width: "))
input_tunas: int = int(input("How many tunas in the simulation? "))
input_sharks: int = int(input("How many sharks in the simulation? "))
input_max_chronons: int = int(input("How many chronons long should the experiment be? "))

planet: World = World(height= input_height, width=input_width)

planet.randomly_place_fishes(nb_sharks = input_sharks, nb_tunas = input_tunas)

step: int = 1

limit: int = input_max_chronons

while planet.chronons < limit:
    planet.run_simulation()
    print("\n")
    print(f"Step {step}:")
    step += 1
    planet.print_grid_ascii()
    