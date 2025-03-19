import pygame, sys

from code.ConstantVariables import WIN_WIDTH, WIN_HEIGHT
from code.Events import Events
from code.Menu import Menu

class Game:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = bool
        self.player = 0
        self.platforms = 0
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu.run()
            Events.handle_events()

    def update(self):
        pass

    def draw(self):
        pass

