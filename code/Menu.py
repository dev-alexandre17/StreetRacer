class Menu

    def __init__(self, screen):
        self.screen = screen
        self.tile: str
        self.options: list[str]
        self.selected_option: int
        self.animation_state: int

    def handle_input(self, event):
        pass

    def update_animation(self):
        pass

    def run(self):
        pass
