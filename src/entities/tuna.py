from __future__ import annotations
from .fish import Fish
from utils.configuration import ConfigurationWator

class Tuna (Fish):
    def __init__(self, pos_x: int, pos_y: int, config: ConfigurationWator)-> None:
        super().__init__(pos_x, pos_y, config)
        self.reproduction_time: int = config.time_breed_tuna
        self.emoji: str ="🐟"

    def reproduce(self, pos_x: int, pos_y: int) -> Tuna | None:
        if self.reproduction_time <= 0:
            self.reproduction_time = self.config.time_breed_tuna
            return Tuna(pos_x, pos_y, self.config)
        self.reproduction_time -= 1
        return None