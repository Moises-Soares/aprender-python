import pygame
import sys
import time
import pymunk

# Importar uma bibliteca que temos no nosso projeto 
# e que tem funcoes que queremos usar
from lib.GameUtil import  GameSprite, Game, Spritesheet

space = pymunk.Space()
space.gravity = (0, 100) 

game = Game(800, 600, space)

# Variaveis para  cores
WHITE = (255, 255, 255)

# Criar um sprite animado
# O sprite animado é um objeto que tem uma imagem e uma posicao
# o primeiro argumento é o caminho para a imagem
# o segundo argumento é a posicao do sprite na imagem
# o terceiro argumento é o tamanho do sprite na imagem
# o quarto argumento é a quantidade de frames que a imagem tem

personagem1SpriteSheet = Spritesheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10)
personagem1 = GameSprite(personagem1SpriteSheet, inicial_position=(100,100))


# tratamento de eventos
def handle_game_event(game, event):
    # tratar direcao do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass
        if event.key == pygame.K_RIGHT:
            pass
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_a:
            pass
        if event.key == pygame.K_d:
            pass
        if event.key == pygame.K_w:
            pass
        if event.key == pygame.K_s:
            pass
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            pass
        if event.key == pygame.K_RIGHT:
            pass
        if event.key == pygame.K_UP:
            pass
        if event.key == pygame.K_DOWN:
            pass
        if event.key == pygame.K_a:
            pass
        if event.key == pygame.K_d:
            pass
        if event.key == pygame.K_w:
            pass
        if event.key == pygame.K_s:
            pass

def update_game_state(game, time_variation):
    personagem1.update()


def render_sprites(game):
    game.screen.fill(WHITE)
    game.screen.blit(personagem1.image, personagem1.rect)
    pygame.display.flip()
    

game.play(handle_game_event, update_game_state, render_sprites)


