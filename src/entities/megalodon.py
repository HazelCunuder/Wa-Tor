from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
from .shark import Shark
from utils.configuration import ConfigurationWator
import random

class Megalodon(Fish):
    def __init__(self, pos_x: int, pos_y: int, config: ConfigurationWator) -> None:
        """
        Initialize a megalodon entity with position and configuration.
        Sets the megalodon's position, configuration, energy, reproduction time, emoji representation, and alive status.
        
        Parameters:
            pos_x (int): The x-coordinate of the megalodon's position in the grid
            pos_y (int): The y-coordinate of the megalodon's position in the grid
            config (ConfigurationWator): Configuration object containing parameters for the megalodon
        """
        
        super().__init__(pos_x, pos_y, config)
        self.energy: int = config.energy_megalodon
        self.reproduction_time: int = config.times_breed_megalodon
        self.emoji: str = "🐋"
        self.is_alive: bool = True


    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        """
        Get the list of available spaces for the megalodon to move to.
        Considers neighboring cells for prey (Tuna, Shark) first, then empty spaces.
        If prey is found, it is prioritized; otherwise, empty spaces are considered.
        If no moves are available, returns an empty list.

        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
        
        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates representing available moves
        """
        
        neighbors = self.get_neighbors(grid)
        preys = []
        empty_box = []
    
        for (x, y) in neighbors:
            cell = grid[y][x]
        
            if cell is None:  
                empty_box.append((x, y))
        
            elif isinstance(cell, (Tuna, Shark)) and cell.is_alive:  
                preys.append((x, y)) 
                
        if preys:
            return preys 
        elif empty_box:
            self.energy -= 1
            return empty_box  
        else:
            self.energy -= 1
            return []
    
    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        """
        Choose a move from the list of available moves, prioritizing prey.
        If no moves are available, the megalodon stays in its current position.
        
        Parameters:
            available_moves (list[tuple[int, int]]): List of possible (x, y
            grid (list[list[Fish | None]]): The current state of the world grid
        
        Returns:
            tuple[int, int]: The chosen (x, y) position to move to
        """
        
        if not available_moves:
            return (self.pos_x, self.pos_y)
        
        x, y = random.choice(available_moves)
        target = grid[y][x]
        
        if isinstance(target, (Tuna, Shark)) and target.is_alive:
            self.eat(grid, x, y)
        
        return (x, y)

    def eat(self, grid: list[list[Fish | None]],pos_x:int, pos_y:int):
        """
        Eat the fish at the specified position, increasing energy and marking it as not alive.
        Increases the megalodon's energy by 1 and sets the target fish's is_alive attribute to False.
        
        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
            pos_x (int): The x-coordinate of the fish to eat
            pos_y (int): The y-coordinate of the fish to eat
        """        
        
        target = grid[pos_y][pos_x]
        if isinstance(target, (Tuna, Shark)) and not isinstance(target, Megalodon):
            self.energy += 1 
            target.is_alive = False 
        
    def reproduce(self, pos_x: int, pos_y: int) -> Fish | None:
        """
        Reproduce a new megalodon at the specified position if reproduction time has elapsed.
        If the reproduction time is zero or less, resets the timer and returns a new Megalodon instance.
        Otherwise, decrements the reproduction timer and returns None.
        
        Parameters:
            pos_x (int): The x-coordinate for the new megalodon's position
            pos_y (int): The y-coordinate for the new megalodon's position  
            
        Returns:
            Fish | None: A new Megalodon instance if reproduction occurs, otherwise None
        """
                
        if self.reproduction_time <= 0:
            self.reproduction_time = self.config.times_breed_megalodon
            return Megalodon(pos_x, pos_y, self.config)
        self.reproduction_time -= 1
        return None
    