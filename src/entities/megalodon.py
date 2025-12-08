from __future__ import annotations
from .fish import Fish
from .tuna import Tuna
from .shark import Shark
import random

class Megalodon(Shark):
    def __init__(self,pos_x:int, pos_y:int) -> None:
        super().__init__(pos_x, pos_y)
        self.energy: int = 3
        self.reproduction_time: int = 7
        self.emoji_shark: str ="🐋"
        self.is_alive: bool = True


    def choose_move():
        pass
    def 