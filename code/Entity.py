from abc import ABC, abstractmethod

import pygame

class Entity(ABC):
    def __init__(self, name: str, position: tuple, speed: int = 0):  # Adiciona speed como opcional
        self.name = name
        self.surface = pygame.image.load(f'asset/{self.name}.png')
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = speed  # Usa o valor passado ou 0 por padrão

    @abstractmethod
    def move(self) -> None:
        pass

    def draw(self, screen) -> None:
        screen.blit(self.surface, self.rect)
