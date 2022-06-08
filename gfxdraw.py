import pygame

from color import Colors

color = Colors()

class gfx(object):
    """ Graphics management """  
         
    def move_surface(self, screen, surface, x = 0, y = 0):
        """ Centers contents of the function to middle of screen. Use x and y to increment """
        xx = surface.get_width()/2 + x
        yy = surface.get_height()/2 + y
        screen.blit(surface, (screen.get_width()/2-xx, screen.get_height()/2-yy))
        
class Button(object):
    def __init__(
        self,
        screen,
        posX:float,
        posY:float,
        button_text:str,
        text_color = (255, 255, 255),
        button_color = (0, 0, 0),
        event = None,
        padding_x:float = 10,
        padding_y:float = 10,
        border_radius = 0
        
    ):
        """"
        Args:
            screen (_type_): The screen or surface the button should be placed on.
            posX (float): X position of button.
            posY (float): Y position of button.
            button_text (str): Button text color.
            text_color (tuple, optional): Text color (R, G, B). Defaults to (255, 255, 255).
            button_color (tuple, optional): Button color (R, G, B). Defaults to (0, 0, 0).
            event (_type_, optional): Runs when button is clicked. Defaults to None if not used.
        """
        
        self.screen     = screen
        font            = pygame.font.SysFont('Corbel', 35)
        text            = font.render(button_text, True, text_color)
        self.width      = text.get_width() + padding_x
        self.height     = text.get_height() + padding_y
        rect            = pygame.Rect(posX,posY, self.width, self.height)
        
        pygame.draw.rect(self.screen, button_color, rect, border_radius=border_radius)
        self.screen.blit(text, (rect.centerx-(text.get_width()/2), (rect.centery-(text.get_height()/2))))

        self.event      = event
        self.rect       = rect
        