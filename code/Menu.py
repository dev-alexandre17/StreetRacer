import pygame.image
import math

from code.ConstantVariables import WIN_WIDTH, COLOR_BLACK, COLOR_WHITE, MENU_OPTIONS, COLOR_YELLOW, COLOR_GRAY
from code.Events import Events

class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.image.load('./asset/Menu-background-game.png')
        self.rect = self.surface.get_rect(left=0, top=0)
        self.tile: str
        self.options = MENU_OPTIONS
        self.selected_option = 0
        self.last_blink_time = pygame.time.get_ticks()
        self.blink_state = True
        self.font = pygame.font.Font(None, 50)

    def handle_input(self, event):
        pass

    def animated_text(self, text, position, color=COLOR_BLACK, amplitude=10, speed=0.005):
        time = pygame.time.get_ticks() * speed
        total_width = sum(self.font.size(letter)[0] for letter in text)
        x_start = (self.screen.get_width() - total_width) // 2
        y = position[1]

        for i, letter in enumerate(text):
            char_surface = self.font.render(letter, True, color)
            offset_y = math.sin(time + i * 0.5) * amplitude  # Animação de sobe e desce
            char_rect = char_surface.get_rect(midtop=(x_start + i * 30, y + offset_y))
            self.screen.blit(char_surface, char_rect)

    def menu_options(self, OPTIONS):
        current_time = pygame.time.get_ticks()
        max_width = max(self.font.size(option)[0] for option in OPTIONS)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if current_time - self.last_blink_time > 500:  # Alterna a cada 500ms
            self.blink_state = not self.blink_state
            self.last_blink_time = current_time

        for i, option in enumerate(OPTIONS):
            color = COLOR_WHITE  # Cor padrão
            if i == self.selected_option:
                color = COLOR_BLACK if self.blink_state else COLOR_WHITE  # Faz piscar

            text_surface = self.font.render(option, True, COLOR_WHITE)
            text_width, text_height = text_surface.get_size()

            x_position = (WIN_WIDTH - max_width) // 1.24
            y_position = 205 + 50 * i

            self.menu_text(32, option, (x_position, y_position), color)

    def play_sound(self):
        pygame.mixer_music.load('./asset/Menu-background-sound.mp3')
        pygame.mixer_music.play(-1)

    def menu_text(self, size, text, position, text_color=COLOR_BLACK):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, text_color)
        text_rect = text_surface.get_rect(midtop=position)
        self.screen.blit(text_surface, text_rect)

    def update(self):
        self.screen.blit(source=self.surface, dest=self.rect)

    def run(self):
        self.play_sound()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_DOWN, pygame.K_s):
                        self.selected_option = (self.selected_option + 1) % len(self.options)
                    if event.key in (pygame.K_UP, pygame.K_w):
                        self.selected_option = (self.selected_option - 1) % len(self.options)
                    if event.key == pygame.K_RETURN:
                        return self.options[self.selected_option]  # Retorna a opção escolhida
            self.update()
            self.animated_text("Street", (self.screen.get_width() // 2.2, 50), color=COLOR_WHITE)
            self.animated_text("Racer", (self.screen.get_width() // 2.2, 115), color=COLOR_WHITE)
            self.menu_options(self.options)
            pygame.display.flip()


