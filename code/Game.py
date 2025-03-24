import pygame, sys
from code.ConstantVariables import WIN_WIDTH, WIN_HEIGHT, MENU_OPTIONS
from code.Events import handle_quit
from code.Menu import Menu
from code.Background import Background  # Importando a classe Background

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.menu = Menu(MENU_OPTIONS)

        # Criando as camadas do fundo com diferentes velocidades
        self.background_layers = [
            Background(f"Level1-{i}", (0, 0), speed=1) for i in range(1)
        ]

        # Controle das faixas da estrada
        self.road_y = 0
        self.road_speed = 5

    def run(self):
        while True:
            menu = Menu(self.screen)
            menu_return = menu.run()

            if menu_return == MENU_OPTIONS[0]:
                self.game_loop()
            elif menu_return == MENU_OPTIONS[1]:
                handle_quit()

    def game_loop(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        # Movimenta cada camada de fundo de forma contínua e suave
        for layer in self.background_layers:
            layer.move()

        # Movimento da estrada (faixas)
        self.road_y += self.road_speed
        if self.road_y >= 40:  # Reinicia a posição das faixas para looping
            self.road_y = 0

    def draw(self):
        # Desenha as camadas de fundo
        for layer in self.background_layers:
            layer.draw(self.screen)

        # Desenha a estrada
        self.draw_road()

        pygame.display.flip()

    def draw_road(self):
        """Desenha uma estrada preta com faixas brancas no meio da tela."""
        road_width = WIN_WIDTH // 3  # Largura da estrada
        lane_width = 10  # Largura das faixas brancas

        # Estrada preta no meio
        pygame.draw.rect(self.screen, (50, 50, 50),
                         (WIN_WIDTH // 3, 0, road_width, WIN_HEIGHT))

        # Linhas laterais brancas
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (WIN_WIDTH // 3, 0, lane_width, WIN_HEIGHT))  # Esquerda
        pygame.draw.rect(self.screen, (255, 255, 255),
                         ((WIN_WIDTH // 3) + road_width - lane_width, 0, lane_width, WIN_HEIGHT))  # Direita

        # Faixas centrais (movendo)
        for i in range(0, WIN_HEIGHT, 80):
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (WIN_WIDTH // 2 - lane_width // 2, i + self.road_y, lane_width, 40))
