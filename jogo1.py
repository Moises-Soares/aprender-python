# pygame abre janela
# pygame desenha retangul

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 400), 0, 32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 100, 100))
    pygame.display.update()


