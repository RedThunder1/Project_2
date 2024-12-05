import pygame

class Button:
    def __init__(self, screen, font, x, y, width, height, text, function):
        """
        Creates clickable button in screen window.
        :param screen: Screen to display button on
        :param x: x coordinate
        :param y: y coordinate
        :param width: button width
        :param height: button height
        :param text: button text
        :param function: function to be run when clicked
        :return: None
        """
        #initialize variables
        self.screen = screen
        self.font = font
        self.x = x - width/2
        self.y = y - height/2
        self.width = width
        self.height = height
        self.text = text
        self.function = function

        self.surface = pygame.Surface((self.width, self.height))
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def process(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.function()

        self.surface = self.font.render(self.text, True, (20,20,20))
        self.screen.blit(self.surface, self.rect)



