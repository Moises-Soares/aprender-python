import pygame
import time
import pymunk
from enum import Enum
import pymunk.pygame_util

class Game:
    def __init__(self, width, height, space = None, debug = False):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.objetcs = []
        self.running = True
        self.last_updated = time.time()
        self.time_variation = 0
        self.space = space
        self.space = pymunk.Space()
        self.debug = debug
        self.background_color = (0,0,0)

    def set_background_color(self, color):
        self.background_color = color

    def play(self, handle_event, update,render, fps=60):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    handle_event(self, event)
            self
            # update game state
            self.time_variation = time.time() - self.last_updated
            if self.space:
                self.space.step(self.time_variation)
            for o in self.objetcs:
                o.update()
            update(self,self.time_variation)
            self.last_updated = time.time()
            # render
            self.screen.fill(self.background_color)
            for o in self.objetcs:
                self.screen.blit(o.image, o.rect)
            if self.debug:
                draw_options = pymunk.pygame_util.DrawOptions(self.screen)
                self.space.debug_draw(draw_options)
            render(self)
            pygame.display.flip()
            #
            self.clock.tick(fps)

    


    def set_gravity(self, gravity):
        self.space.gravity = gravity
        
    def add_game_object(self, gameObject ):
         gameObject.body = pymunk.Body(gameObject.mass, pymunk.moment_for_box(gameObject.mass, gameObject.image.get_size()))
         gameObject.body.position = pymunk.Vec2d(gameObject.rect.x, gameObject.rect.y)
         gameObject.body.body_type = gameObject.body_type.value
         gameObject.shape = pymunk.Poly.create_box(gameObject.body, gameObject.image.get_size() )
         self.objetcs.append(gameObject)
         self.space.add(gameObject.body, gameObject.shape)

    def add_game_objects(self, gameObjects):
        for o in gameObjects:
            self.add_game_object(o)



class SpriteSheet:
    def __init__(self, path, start=(0, 0), frame_size=(32, 32), frame_number=1):
        self.path = path
        self.start = start
        self.frame_size = frame_size
        self.frame_number = frame_number




class GameObjectType(Enum):
    DYNAMIC = pymunk.Body.DYNAMIC
    STATIC = pymunk.Body.STATIC
    KINEMATIC = pymunk.Body.KINEMATIC

class GameObject(pygame.sprite.Sprite):    
    def __init__(self, position = (0,0), size=(32,32), type=GameObjectType.DYNAMIC):
        super().__init__()

        self.position = position
        self.size = size
        self.type = type

        #
        self.spriteSheet = None
        self.inicial_position = (0,0)
        self.space = None
        self.mass = 1
        self.body_type = type
        self.animation_speed = 0.2 
        self.last_updated = time.time()
        self.sheet = {}
        self.animations = {}
        self.current_animation = None
        self.current_frame = 0
        self.rect = pygame.Rect(position, size) 
        


    def add_animation(self, name, spriteSheet):
        # Load the image from the sprite sheet path
        sheet_image = pygame.image.load(spriteSheet.path).convert_alpha()

        frame_dimensions = [(spriteSheet.start[0] + i * spriteSheet.frame_size[0], spriteSheet.start[1], spriteSheet.frame_size[0], spriteSheet.frame_size[1]) for i in range(spriteSheet.frame_number)]
        frames = []
        for (x, y, width, height) in frame_dimensions:
            sprite = pygame.Surface((width, height), pygame.SRCALPHA)
            sprite.blit(sheet_image, (0, 0), (x, y, width, height))  # Use the loaded image here
            frames.append(sprite)
        self.animations[name] = frames

    def set_current_animation(self, name):
        self.current_animation = name
        self.current_frame = 0
        self.image = self.animations[self.current_animation][self.current_frame]
        self.last_updated = time.time() 
        


    def update(self):
        # Update sprite animation
        if time.time() - self.last_updated > self.animation_speed:
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]
            self.last_updated = time.time()

        # Update sprite position based on physics
        if hasattr(self, 'body'):
            self.rect.x = self.body.position.x - self.rect.width / 2
            self.rect.y = self.body.position.y - self.rect.height / 2

    def apply_force(self, force):
        self.body.apply_force_at_local_point(force)

    def clone(self, position=(0,0)):
        clone = GameObject(position, self.size, self.type)
        clone.spriteSheet = self.spriteSheet
        clone.inicial_position = self.inicial_position
        clone.space = self.space
        clone.mass = self.mass
        clone.body_type = self.body_type
        clone.animation_speed = self.animation_speed
        clone.last_updated = self.last_updated
        clone.sheet = self.sheet
        clone.animations = self.animations
        clone.current_animation = self.current_animation
        clone.current_frame = self.current_frame
        clone.rect = self.rect
        clone.type = self.type
        return clone

    

    
