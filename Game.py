import pygame
import sys
import time
import pymunk

# Importar uma bibliteca que temos no nosso projeto 
# Game é uma classe que representa o jogo
# GameObject é uma classe que representa um objeto do jogo
# SpriteSheet é uma classe que representa uma imagem com varios frames
from lib.GameUtil import  GameObject, Game, SpriteSheet


game = Game(800, 600)
game.gravity((0, 10))

# Variaveis para  cores
WHITE = (255, 255, 255)
FORCA_DO_SALTO = 500 

personagem1SpriteSheet = SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10)
personagem1 = GameObject(personagem1SpriteSheet, inicial_position=(100,100))

personagem2 = personagem1.clone((200, 100))

game.add_game_object(personagem1)
game.add_game_object(personagem2)

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
        if event.key == pygame.K_SPACE:
             personagem1.apply_force((0, -FORCA_DO_SALTO))
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
    personagem2.update()


def render_sprites(game):
    game.screen.fill(WHITE)
    game.screen.blit(personagem1.image, personagem1.rect)
    game.screen.blit(personagem2.image, personagem2.rect)
    pygame.display.flip()
    

game.play(handle_game_event, update_game_state, render_sprites)


