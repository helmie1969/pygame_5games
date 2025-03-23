# Import
import pygame
from configuration import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Eigenschaften
        self.image = pygame.image.load("space shooter/images/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=[WINDOW_WIDTH/2, WINDOW_HEIGHT/2])

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= PLAYER_SPEED
            if self.rect.bottom <= 37: self.rect.bottom = 37
        if keys[pygame.K_s]:
            self.rect.y += PLAYER_SPEED
            if self.rect.top >= WINDOW_HEIGHT - 37: self.rect.top = WINDOW_HEIGHT - 37
        if keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
            if self.rect.right <= 56: self.rect.right = 56
        if keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED
            if self.rect.left >= WINDOW_WIDTH - 56: self.rect.left = WINDOW_WIDTH - 56

    def update(self):
        self.player_input()
