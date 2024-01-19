import pygame
from lib.GameUtil import  GameObject, Game, GameObjectType, SpriteSheet

WHITE = (255, 255, 255)

game = Game(800, 600)
game.set_gravity((0, 10))
game.set_background_color(WHITE)

# Variaveis para  cores

FORCA_DO_SALTO = 500 

personagem1SpriteSheet = SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10)
personagem1 = GameObject(personagem1SpriteSheet, inicial_position=(100,100))

blocoSpriteSheet = SpriteSheet("sprites/PixelAdventure/Terrain/Terrain (16x16).png", (0,0), (48,48), 1)
bloco = GameObject(blocoSpriteSheet, inicial_position=(100,200), type=GameObjectType.STATIC)
bloco2 = bloco.clone((300,300))

game.add_game_object(personagem1)
game.add_game_object(bloco)
game.add_game_object(bloco2)

# tratamento de eventos
def handle_game_event(game, event):
    # tratar direcao do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass
        if event.key == pygame.K_RIGHT:
            personagem1.apply_force((100, 0))
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
    pass


def render_sprites(game):
    pass
    

game.play(handle_game_event, update_game_state, render_sprites)


