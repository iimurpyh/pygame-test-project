import src.objects as objects
import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

FPS = 60

def create_test_map():
    objects.Platform(pygame.Rect(0, 300, 400, 30))
    objects.Player(pygame.Rect(25,0,15,30))

def run():
    running = True
    while running:
        dt = clock.tick(FPS) / 1000
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Update game objects
        for gameObject in objects.GameObject.gameObjects:
            gameObject.update(dt)
    
        # Fill background
        screen.fill((255, 255, 255))

        # Draw game objects
        for gameObject in objects.GameObject.gameObjects:
            gameObject.draw(screen)

        pygame.display.flip()

create_test_map()
run()

pygame.quit()