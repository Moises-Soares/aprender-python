import pygame
from GameUtil import  GameObject, Game, GameObjectType, SpriteSheet

WHITE = (255, 255, 255)

game = Game(800, 600)
game.set_gravity((0, 10))
game.set_background_color(WHITE)

FORCA_DO_SALTO = 500 

personagem1 = GameObject(position=(100,100), size=(32,32), type=GameObjectType.DYNAMIC)
personagem1.add_animation("idle", SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Idle (32x32).png", (0,0), (32,32), 10))
personagem1.add_animation("run", SpriteSheet("sprites/PixelAdventure/Main Characters/Ninja Frog/Run (32x32).png", (0,0), (32,32), 10))
personagem1.set_current_animation("idle")

bloco = GameObject(position=(100,400), size=(40,48), type=GameObjectType.STATIC)
bloco.add_animation("idle", SpriteSheet("sprites/PixelAdventure/Terrain/Terrain (16x16).png", (0,0), (48,48), 1))
bloco.set_current_animation("idle")

game.add_game_object(personagem1)
game.add_game_object(bloco)


# tratamento de eventos
def handle_game_event(game, event):
    # tratar direcao do personagem
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            pass
        if event.key == pygame.K_RIGHT:
            personagem1.apply_force((500, 0))
            personagem1.set_current_animation("run")
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


