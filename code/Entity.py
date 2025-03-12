class Entity:

    def __init__(self, x: int, y: int, width: int, height: int, velocity_y: float, velocity_x: float):
        self.position_x = x
        self.position_y = y
        self.width = width
        self.height = height
        self.velocity_y = velocity_y
        self.velocity_x = velocity_x

    def move(self) -> None:
        pass

    def draw(self, screen) -> None:
        pass
