class Menu

    def __init__(self):
        self.tile: str
        self.options: list[str]
        self.selected_option: int
        self.animation_state: int

    def display(self, screen):
        pass

    def handle_input(self, event):
        pass

    def update_animation(self):
        pass
