from __future__ import annotations
from .fish import Fish
from utils.configuration import ConfigurationWator

class Tuna (Fish):
    def __init__(self, pos_x: int, pos_y: int, config: ConfigurationWator)-> None:
        """
        Initialize a tuna entity with position and configuration.
        Sets the tuna's position, configuration, reproduction time, emoji representation.
        
        Parameters:
            pos_x (int): The x-coordinate of the tuna's position in the grid
            pos_y (int): The y-coordinate of the tuna's position in the grid
            config (ConfigurationWator): Configuration object containing parameters for the tuna
        """        
        
        super().__init__(pos_x, pos_y, config)
        self.reproduction_time: int = config.time_breed_tuna
        self.emoji: str ="🐟"

    def reproduce(self, pos_x: int, pos_y: int) -> Tuna | None:
        """
        Handle the reproduction process for the tuna.
        If the reproduction time has reached zero, creates a new Tuna at the specified position
        and resets the reproduction timer. Otherwise, decrements the timer.
        
        Parameters:
            pos_x (int): The x-coordinate
            pos_y (int): The y-coordinate
            
        Returns:
            Tuna | None: A new Tuna instance if reproduction occurs, otherwise None
        """        
        
        if self.reproduction_time <= 0:
            self.reproduction_time = self.config.time_breed_tuna
            return Tuna(pos_x, pos_y, self.config)
        self.reproduction_time -= 1
        return None