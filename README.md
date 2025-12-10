# Wa-Tor

Wa-Tor is a predator-prey simulation that models the interactions between sharks, tunas, and megalodons in a grid-based ocean environment. The simulation allows users to observe how these species coexist, reproduce, and compete for resources over time.

## Features

- Grid-based world representation
- Entities: Sharks, Tunas, and Megalodons with unique behaviors
- Configurable parameters for reproduction, energy, and movement
- Save simulation data to a PostgreSQL database for analysis

## Project Structure

- `assets/`: Contains any assets used in the project (e.g., images, icons).
- `src/`: Contains the main source code for the simulation.
  - `entities/`: Contains classes for different fish entities (Shark, Tuna, Megalodon).
    - `fish.py`: Base class for fish entities.
    - `shark.py`: Contains the Shark class with specific behaviors.
    - `tuna.py`: Contains the Tuna class with specific behaviors.
    - `megalodon.py`: Contains the Megalodon class with specific behaviors.
  - `utils/`: Contains utility classes for configuration and data management.
    - `configuration.py`: Contains the ConfigurationWator class for simulation parameters.
    - `data_manager.py`: Contains the DataManager class for database interactions.
  - `main.py`: The main script to run the simulation.
  - `simulation.py`: Contains the Simulation class that manages the simulation loop.
  - `world.py`: Contains the World class that represents the grid and manages entity placement and movement.
- `Readme.md`: This file, providing an overview of the project.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HazelCunuder/Wa-Tor.git
   cd Wa-Tor
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up PostgreSQL database and update the configuration in `utils/data_manager.py` if necessary.

## Usage

Run the main simulation script:

```bash
python src/main.py
```

## Configuration

You can adjust the simulation parameters in the `ConfigurationWator` class when you start a simulation in `src/main.py`. Parameters include:

- Number of sharks, tunas, and megalodons
- Reproduction times
- Energy levels
- Grid size

## Contributors

- Hazel Cunuder - [GitHub](https://github.com/HazelCunuder)

  - Created the World, Simulation, and DataManager classes.
  - Implemented the main simulation loop and database interactions.
  - Made this README file.

- Sarah Azzi - [GitHub](https://github.com/SarahAzzI)

  - Added the Megalodon entity and its behaviors.
  - Added the configuration file for simulation parameters.

- Alexandre Crestien - [GitHub](https://github.com/AlexandreCrestien)

  - Created Fish, Shark and Tuna entity classes with their specific behaviors.
  - Implemented movement, reproduction, and eating logic for entities.
  - Created the User Interface for visualizing the simulation.
