import src.objects as objects
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400))

def create_test_map():
    objects.Platform(pygame.Rect(0, 70, 100, 30))

def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    
        # Fill background
        screen.fill((255, 255, 255))

        # Update game objects
        for gameObject in objects.GameObject.gameObjects:
            gameObject.draw(screen)

        pygame.display.flip()

create_test_map()
run()

pygame.quit()