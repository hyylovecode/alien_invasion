from typing import Any
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  def __init__(self, ai_game):
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings

    self.image = pygame.image.load('images/alien.png')
    
    self.scales_width = 60
    self.scales_height = 60

    self.image = pygame.transform.scale(self.image, (self.scales_width, self.scales_height))
    self.rect = self.image.get_rect()

    self.rect.x = 0
    self.rect.y = 0

    self.x = float(self.rect.x)

  def check_edges(self):
    if self.rect.right >= self.screen.get_rect().right or self.rect.left <= 0:
      return True

  def update(self):
    self.rect.x += self.settings.alien_speed * self.settings.fleet_direction