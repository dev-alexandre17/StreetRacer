class Player:

    def __init__(self):
        self.health = int
        self.speed = float
        self.jump_power = float
        self.gravity = float
        self.velocity_y = float
        self.velocity_x = float
        self.on_ground = bool

    def move(self, keys) -> None:
        pass

    def apply_gravity(self, platforms) -> None:
        pass

    def take_damage(self, amount: int) -> None:
        pass

    def draw(self, screen) -> None:
        pass