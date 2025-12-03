class World:
    def __init__(self, height: int, width: int) -> None:
        self.grid_height: int = height
        self.grid_width: int = width
        self.grid = self.init_grid()
        self.chronons: int = 0
        self.tunas = []
        self.sharks = []
        
    def init_grid(self) -> list[list[str]]:
        # We use _ here because we won't use this variable for anything else in the entire code
        return [[" " for _ in range(self.grid_width)] for _ in range(self.grid_height)]