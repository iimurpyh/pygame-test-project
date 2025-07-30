import pygame
from pygame.locals import *

COLOR_PLATFORMS = pygame.Color(0, 0, 0)
COLOR_PLAYER = pygame.Color(255,0,0)

GRAVITY = 1

class GameObject():
    gameObjects = []

    def __init__(self, rect):
        GameObject.gameObjects.append(self)
        self.rect = rect
    
    def draw(self, surface):
        pass

    def update(self, dt):
        pass
    

class Platform(GameObject):
    platforms = []

    def __init__(self, rect):
        super().__init__(rect)
        Platform.platforms.append(self)

    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_PLATFORMS, self.rect)

class Player(GameObject):
    JUMP_POWER = 10
    X_ACCELERATION = 1
    X_MAXSPEED = 6
    Y_MAXSPEED = 30

    def __init__(self, rect):
        super().__init__(rect)
        self.yVelocity = 0
        self.xVelocity = 0
        self.grounded = True
    
    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_PLAYER, self.rect)
    
    def jump(self):
        self.yVelocity = -12
        self.grounded = False

    def isTouchingPlatform(self):
        
        return self.rect.collidelist(Platform.platforms) != -1
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[K_UP] and self.grounded:
            self.jump()
        
        if keys[K_LEFT]:
            self.xVelocity -= self.X_ACCELERATION
        elif keys[K_RIGHT]:
            self.xVelocity += self.X_ACCELERATION
        else:
            self.xVelocity *= 0.6
        
        if self.xVelocity > self.X_MAXSPEED:
            self.xVelocity = self.X_MAXSPEED
        if self.xVelocity < -self.X_MAXSPEED:
            self.xVelocity = -self.X_MAXSPEED
        
        self.rect.x += self.xVelocity
        if self.isTouchingPlatform():
            self.rect.x -= self.xVelocity
        
        self.rect.y += self.yVelocity
        if self.isTouchingPlatform():
            self.grounded = True
            self.rect.y -= self.yVelocity
            self.yVelocity = 0
        else:
            self.grounded = False
        
        self.yVelocity += GRAVITY
        if self.yVelocity > self.Y_MAXSPEED:
            self.yVelocity = self.Y_MAXSPEED