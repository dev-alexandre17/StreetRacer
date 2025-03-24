import os

from code.Background import Background

class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        list_entities = []
        i = 0

        while True:
            image_path = f"./asset/{entity_name}-{i}.png"

            if os.path.exists(image_path):
                entity = Background(f"{entity_name}-{i}", position, speed=3)  # Criando a entidade corretamente
                list_entities.append(entity)  # Adicionando à lista
                i += 1
            else:
                break

        return list_entities