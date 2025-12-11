from world import World
from simulation import Simulation
from utils.configuration import ConfigurationWator
from simulation_graph import SimulationGraph
from interface_graphique import InterfaceGraphique


def ask_mode() -> str:
    while True:
        print("=== Choose a mode ===")
        print("1 → Terminal (ASCII)")
        print("2 → Graphical Interface (Tkinter)")

        choice = input("Your choice (1/2): ").strip()

        if choice in ("1", "2"):
            return choice

        print("Invalid choice, please enter 1 or 2.\n")


def run_gui_mode() -> None:
    app = InterfaceGraphique()
    app.mainloop()


def run_terminal_mode() -> None:
    config = ConfigurationWator()

    world: World = World(config)
    world.randomly_place_fishes(
        nb_sharks=config.nb_shark,
        nb_tunas=config.nb_tuna,
        nb_megalodons=config.nb_megalodon,
    )

    graph = SimulationGraph()
    simulation = Simulation(world, graph)

    simulation.run_simulation(world, graph)


def main() -> None:
    mode = ask_mode()

    if mode == "2":
        run_gui_mode()
    else:
        run_terminal_mode()


if __name__ == "__main__":
    main()
