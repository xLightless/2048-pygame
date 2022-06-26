import pygame
# import pygame.freetype
import random

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
        text_color          = (255, 255, 255),
        button_color        = (0, 0, 0),
        event               = None,
        padding_x:float     = 10,
        padding_y:float     = 10,
        border_radius       = 0,
        hide                = False
        
    ):
        """"
        Args:
            screen (_type_): The screen or surface the button should be placed on.
            posX (float): X position of button.
            posY (float): Y position of button.
            button_text (str): Button text color.
            text_color (tuple, optional): Text color (R, G, B). Defaults to (255, 255, 255).
            button_color (tuple, optional): Button color (R, G, B). Defaults to (0, 0, 0).
            event (_type_, optional): Runs when button is clicked. Defaults to None if not used explictly.
        """
        if hide == False:            
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
        
    # def callback(callback):
    #     """ Used to run the operation of the button or event """
    #     if type(callback) == str:
    #         print(callback)
    #     else:
    #         return callback

class Grid(object):
    """ Old prototype of the grid """
    def __init__(
        self,
        screen,
        grid_x = 4,
        grid_y = 4,
        border_color = color.GRAY,
        block_color = color.OLD_LAVENDER,
        grid_square_size:int= 128
    ):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.grid_square_size = grid_square_size
        # self.font           = pygame.font.Font('Corbel', 35)
        
        background = pygame.Surface((grid_square_size*grid_x, grid_square_size*grid_y))
        bg_width, bg_height = background.get_width(), background.get_height()
        background.fill((block_color))
        block_positions = []
        for x in range(0, grid_x):
            for y in range(0, grid_y):
                rect_block = pygame.Rect(x*grid_square_size, y*grid_square_size, grid_square_size, grid_square_size)
                block = pygame.draw.rect(background, border_color, rect_block, 4)
                block_positions.append((block.centerx, block.centery))

                # text = self.font.render('test', True, color.WHITE, None)
                

        screen.blit(background, (self.width/2-bg_width/2, self.height/2-bg_height/2))
        self.block_positions_ = block_positions