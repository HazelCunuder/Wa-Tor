from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
from utils.configuration import ConfigurationWator
import random

class Shark(Fish):
    def __init__(self, pos_x: int, pos_y: int, config: ConfigurationWator)-> None:
        """
        Initialize a shark entity with position and configuration.
        Sets the shark's position, configuration, energy, reproduction time, emoji representation.
        
        Parameters:
            pos_x (int): The x-coordinate of the shark's position in the grid
            pos_y (int): The y-coordinate of the shark's position in the grid
            config (ConfigurationWator): Configuration object containing parameters for the shark
        """
                        
        super().__init__(pos_x, pos_y, config)
        self.energy: int = config.energy_shark
        self.reproduction_time: int = config.times_breed_shark
        self.emoji: str ="🦈"
    
    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        """
        Choose a move from the list of available moves.
        If a tuna is available in the moves, eat it and move there.
        
        Parameters:
            available_moves (list[tuple[int, int]]): List of possible (x, y
            grid (list[list[Fish | None]]): The current state of the world grid
            
        Returns:
            tuple[int, int]: The chosen (x, y) position to move to
        """
        
        if not available_moves:
            return (self.pos_x, self.pos_y)

        if isinstance(grid[available_moves[0][1]][available_moves[0][0]], Tuna):
            x, y = random.choice(available_moves)
            tuna = grid[y][x]
            self.eat(tuna)  
            return (x, y)

        return super().choose_move(available_moves, grid)

    def eat(self, tuna: Tuna) -> None:
        """
        Eat the specified tuna, increasing energy and marking it as not alive.
        Increases the shark's energy by the configured recovery amount and sets the tuna's is_alive attribute to False.
        
        Parameters:
            tuna (Tuna): The tuna entity to eat
        """
        
        tuna.is_alive = False
        self.energy += self.config.recovery_energy_shark

    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        """
        Get the list of available spaces for the shark to move to.
        Considers neighboring cells for tuna first, then empty spaces.
        If tuna is found, it is prioritized; otherwise, empty spaces are considered.
        If no moves are available, decreases energy and checks for death.
        
        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
            
        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates representing available moves
        """        
        
        available: list[tuple[int, int]] = []
        neighbors: list[tuple[int, int]] = self.get_neighbors(grid)
    
        for (x, y) in neighbors:
            cell : Fish | None = grid[y][x]
            if isinstance(cell, Tuna) and cell.is_alive:
                available.append((x, y))

        if available:
            return available
        else:
            self.energy -= 1
            if self.energy <= 0:
                self.is_alive = False
            return super().get_available_spaces(grid)
        
    def reproduce(self, pos_x: int, pos_y: int) -> Shark | None:
        """
        Reproduce a new shark at the specified position if reproduction time has elapsed.
        If the reproduction cooldown has reached zero, creates a new Shark instance at the given position
        and resets the reproduction timer. Otherwise, decrements the timer and returns None.
        
        Parameters:
            pos_x (int): The x-coordinate for the new shark's position
            pos_y (int): The y-coordinate for the new shark's position
            
        Returns:
            Shark | None: A new Shark instance if reproduction occurs, otherwise None
        """
        
        if self.reproduction_time <= 0:
            self.reproduction_time = self.config.times_breed_shark
            return Shark(pos_x, pos_y, self.config)
        
        self.reproduction_time -= 1
        return None 