class Enemy:

    def __init__(self, x: int, y: int, width: int, height: int, speed: float, direction: int):
        self.position_x = x
        self.position_y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.direction = direction