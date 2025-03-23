# Import
import pygame
from configuration import *
from classes import *

# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pygame Space Shooter")
clock = pygame.time.Clock()
running = True

# Sprite-Groups
player = pygame.sprite.GroupSingle()
player.add(Player())


# Game Loop
while running:
    # Eventloop
    for event in pygame.event.get():
        # pygame.QUIT event means the user clicked X to close your window
        if event.type == pygame.QUIT: 
            running = False
        
    # Drawing
    screen.fill("darkgrey")
    player.draw(screen)
    player.update()

    # Display update
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()