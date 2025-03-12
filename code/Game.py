import pygame, sys

from code.Menu import Menu


class Game:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = bool
        self.player = 0
        self.platforms = 0
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu.run()
            pass
            # Check for all events
            #f or event in pygame.event.get():
                # if event.type == pygame.QUIT:
                    # pygame.quit()  # Close Window
                    # sys.exit()  # End pygame

    def handle_events(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

