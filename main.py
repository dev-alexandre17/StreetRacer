import sys

import pygame

pygame.init()
print('Setup Start')
window = pygame.display.set_mode((800, 600))
print('Setup End')

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Close Window
            sys.exit() # End pygame