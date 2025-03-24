import pygame
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position)
        self.speed = speed
        self.height = self.surface.get_height()  # Usar surface da Entity
        self.rect = self.surface.get_rect(topleft=position)

    def move(self):
        """Move o fundo para baixo, reiniciando quando sai da tela."""
        self.rect.y += self.speed

        # Se a imagem sair completamente da tela, reposiciona no topo
        if self.rect.y >= self.height:
            self.rect.y = -self.height

    def draw(self, screen):
        """Desenha o fundo e cria um efeito contínuo."""
        screen.blit(self.surface, (self.rect.x, self.rect.y))