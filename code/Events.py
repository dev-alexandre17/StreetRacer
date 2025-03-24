import pygame
import sys

def handle_quit():
    pygame.quit()
    sys.exit()

class Events:
    @staticmethod
    def handle_events(menu_instance):  # Recebe uma instância do Menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_DOWN, pygame.K_s):
                    menu_instance.selected_option = (menu_instance.selected_option + 1) % len(menu_instance.options)
                if event.key in (pygame.K_UP, pygame.K_w):
                    menu_instance.selected_option = (menu_instance.selected_option - 1) % len(menu_instance.options)
                if event.key == pygame.K_RETURN:
                    return menu_instance.options[menu_instance.selected_option]

