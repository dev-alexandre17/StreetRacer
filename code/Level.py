import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory

class Level:
    def __init__(self, window, name, menu_option):
        if not isinstance(window, pygame.Surface):
            raise TypeError(f"Erro: window deve ser pygame.Surface, mas recebeu {type(window)}")

        self.window = window
        self.name = name
        self.menu_option = menu_option
        self.entity_list = []

        # Obtém entidades da fábrica e verifica se são válidas
        entities = EntityFactory.get_entity("Level1")
        print(f"Entidades carregadas: {entities}")  # Depuração

        # Garante que apenas objetos da classe Entity sejam adicionados
        for entity in entities:
            if isinstance(entity, Entity):
                self.entity_list.append(entity)
            else:
                print(f"⚠️ Atenção: entidade inválida detectada -> {entity}")

    def load_level(self):
        if not isinstance(self.window, pygame.Surface):
            raise TypeError(f"Erro: self.window deveria ser pygame.Surface, mas é {type(self.window)}")

        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surface, dest=ent.rect)
            pygame.display.flip()

    def draw(self):
        """Desenha o nível na tela."""
        self.window.fill((0, 100, 0))  # Fundo verde (grama)
        for ent in self.entity_list:
            self.window.blit(ent.surface, ent.rect)