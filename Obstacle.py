import pygame
import random

class Obstacle:
    def __init__(self, screen, scroll_speed):
        """
        Creates obstacle for player to avoid.
        :param screen: Screen to display obstacle on
        :param scroll_speed: the speed the obstacles move to the side
        :return: None
        """
        self.screen = screen
        self.scroll_speed = scroll_speed

        #Randomly generate the height of the gap
        height = random.randint(100, 300)
        self.upper_surface = pygame.Surface((50, height))
        self.lower_surface = pygame.Surface((50, 400 - height))
        self.upper_rect = pygame.Rect(550, 0, self.upper_surface.get_width(), height)
        self.lower_rect = pygame.Rect(550, height + 100, self.lower_surface.get_width(), 400 - height)



    def process(self):
        self.upper_surface.fill("green")
        self.lower_surface.fill("green")

        #scroll obstacles
        self.upper_rect.x -= self.scroll_speed
        self.lower_rect.x -= self.scroll_speed

        self.screen.blit(self.upper_surface, (self.upper_rect.x, self.upper_rect.y))
        self.screen.blit(self.lower_surface, (self.lower_rect.x, self.lower_rect.y))

    def check_collision(self, player_pos):
        if self.upper_rect.collidepoint(player_pos) or self.lower_rect.collidepoint(player_pos):
            return True
