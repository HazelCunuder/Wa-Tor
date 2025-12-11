from __future__ import annotations
from utils.configuration import ConfigurationWator
import random

class Fish:
    def __init__(self, pos_x: int , pos_y: int, config: ConfigurationWator)-> None:
        """
        Initialize a fish entity with position and configuration.
        Sets the fish's position, configuration, alive status, and default emoji representation.
        
        Parameters:
            pos_x (int): The x-coordinate of the fish's position in the grid
            pos_y (int): The y-coordinate of the fish's position in the grid
            config (ConfigurationWator): Configuration object containing parameters for the fish
        """
        
        self.pos_x: int = pos_x
        self.pos_y: int = pos_y
        self.config = config 
        self.is_alive: bool = True
        self.emoji: str = " "
        
    def move(self, grid:  list[list[Fish | None]]) -> tuple[int, int]:
        """
        Move the fish to a new position based on available spaces in the grid.
        Determines available moves, chooses one, updates position, and returns the new coordinates.
        
        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
        Returns:
            tuple[int, int]: The new (x, y) position of the fish after moving
        """
        
        available_moves : list[tuple[int, int]] = self.get_available_spaces(grid)
        move: tuple[int, int] = self.choose_move(available_moves, grid)
        self.pos_x, self.pos_y = move
        return move

    def choose_move(self, available_moves: list[tuple[int, int]], grid: list[list[Fish | None]]) -> tuple[int, int]:
        """
        Choose a move from the list of available moves.
        If no moves are available, the fish stays in its current position.
        
        Parameters:
            available_moves (list[tuple[int, int]]): List of possible (x, y
            grid (list[list[Fish | None]]): The current state of the world grid
            
        Returns:
            tuple[int, int]: The chosen (x, y) position to move to
        """
        
        if not available_moves:
            return (self.pos_x, self.pos_y)
        return random.choice(available_moves)
    
    def get_neighbors(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        """
        Get the coordinates of neighboring cells in the grid, wrapping around edges.
        Considers the four cardinal directions (up, down, left, right) and uses modulo
        arithmetic to wrap around the grid edges.
        
        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
            
        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates of neighboring cells
        """
        
        height:  int = len(grid)
        width:  int = len(grid[0])
        neighbors:  list[tuple[int, int]] = [
            ((self.pos_x + 1) % width, self.pos_y),
            ((self.pos_x - 1) % width, self.pos_y),
            (self.pos_x, (self.pos_y + 1) % height),
            (self.pos_x, (self.pos_y - 1) % height)
        ]
        return neighbors
    
    def get_available_spaces(self, grid: list[list[Fish | None]]) -> list[tuple[int, int]]:
        """
        Get a list of available (empty) neighboring spaces in the grid.
        Checks neighboring cells and collects coordinates of those that are empty (None).
        
        Parameters:
            grid (list[list[Fish | None]]): The current state of the world grid
            
        Returns:
            list[tuple[int, int]]: List of (x, y) coordinates of available empty spaces
        """
        neighbors:  list[tuple[int, int]] = self.get_neighbors(grid)
        available:  list[tuple[int, int]] = []

        for (x, y) in neighbors:
            if grid[y][x] is None :
                available.append((x, y))
        return available

    def reproduce(self, pos_x: int, pos_y: int) -> Fish | None:
        """
        Handle reproduction logic for the fish.
        This method should be overridden by subclasses to implement species-specific reproduction behavior.
        
        Parameters:
            pos_x (int): The x-coordinate for the offspring's position
            pos_y (int): The y-coordinate for the offspring's position
            
        Returns:
            Fish | None: A new Fish instance if reproduction occurs, otherwise None
            
        Raises:
            NotImplementedError: This method should be implemented by subclasses
        """
        
        raise NotImplementedError