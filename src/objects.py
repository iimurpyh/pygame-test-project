import pygame

COLOR_PLATFORMS = pygame.Color(0, 0, 0)
COLOR_PLAYER = pygame.Color(255,0,0)

class GameObject():
    gameObjects = []

    def __init__(self, rect):
        GameObject.gameObjects.append(self)
        self.rect = rect
    
    def draw(self):
        pass
    

class Platform(GameObject):
    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_PLATFORMS, self.rect)

class Player(GameObject):
    def draw(self, surface):
        pygame.draw.rect(surface, COLOR_PLAYER, self.rect)