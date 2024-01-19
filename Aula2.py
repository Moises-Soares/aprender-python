import pygame
import sys

# Importar uma bibliteca que temos no nosso projeto 
# e que tem funcoes que queremos usar
from lib.GameUtil import  AnimatedSprite, Game

game = Game(800, 600)

# Variaveis para  cores
WHITE = (255, 255, 255)

# Criar um sprite animado
# O sprite animado é um objeto que tem uma imagem e uma posicao
personagem1 = AnimatedSprite("sprites/PixelAdventure/Main Characters/Mask Dude/Idle (32x32).png", (0,0), (32,32), 10)
personagem1.rect.x = 100
personagem1.rect.y = 100

personagem2 = AnimatedSprite("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10)
personagem2.rect.x = 200
personagem2.rect.y = 200

fundo = AnimatedSprite("sprites/PixelAdventure/Background/Blue.png", (0,0), (32,32), 1)
fundo.rect.x = 0
fundo.rect.y = 0

# tratamento de eventos
def handle_game_event(game, event):
    # tratar direcao do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            personagem1.rect.x -= 10
        if event.key == pygame.K_RIGHT:
            personagem1.rect.x += 10
        if event.key == pygame.K_UP:
            personagem1.rect.y -= 10
        if event.key == pygame.K_DOWN:
            personagem1.rect.y += 10
        if event.key == pygame.K_a:
            personagem2.rect.x -= 10
        if event.key == pygame.K_d:
            personagem2.rect.x += 10
        if event.key == pygame.K_w:
            personagem2.rect.y -= 10
        if event.key == pygame.K_s:
            personagem2.rect.y += 10

def update_game_state(game):
    personagem1.update()
    personagem2.update()
    fundo.update()
    pass


def render_sprites(game):
    game.screen.fill(WHITE)
    game.screen.blit(personagem1.image, personagem1.rect)
    pygame.display.flip()
    

game.play(handle_game_event, update_game_state, render_sprites)


