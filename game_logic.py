import random
import pygame

from color import Colors

color = Colors()

class GRID_ARRAY(object):
    """ Parent class for game grid """
    def __init__(
        self,
        screen,
        size,
        grid_x,
        grid_y,
        border = True
    ):
        self.grid_x = grid_x
        self.grid_y = grid_y
        
        blocks:int = grid_x*grid_y
        block_list = []

        terminated = False
        while not terminated:
            x = random.randint(0, blocks)
            y = random.randint(0, blocks)
            if x!=y:
                terminated = True
                
            for _ in range(0, blocks):
                block_list.append(0)
            
            # Gets the length of block list and finds the XY values and sets them to 1, keeping the rest at 0.
            for item in range(len(block_list)):
                if item == x:
                    block_list[item] = 1
                    self.x = item
                    
                if item == y:
                    block_list[item] = 1
                    self.y = item

        self.positions = (x,y) # List position of starting points
        self.block_list = block_list
        self.screen = screen
        self.size = size
        self.border = border
        
    def draw(self):
        # These will be used for drawing objects to grid array
        self.list_rect_x = []
        self.list_rect_y = []
        
        # Padding options for moving objects
        self.grid_paddingx = (((self.screen.get_width())-self.grid_x*self.size[0])/2)
        self.grid_paddingy = (((self.screen.get_height())-self.grid_y*self.size[1])/2)
        grid_border = 22

        # Background border for the grid
        if self.border == True:
            self.background = pygame.Rect(self.grid_paddingx-(grid_border/2), self.grid_paddingy-(grid_border/2), 
                                      self.grid_x*self.size[0]+grid_border, self.grid_y*self.size[1]+grid_border)
            pygame.draw.rect(self.screen, color.border_color, self.background, border_radius = 8)
        
        # Draws grid x, grid y, to the screen
        for gx in range(0, self.grid_x):
            for gy in range(0, self.grid_y):
                
                self.image = pygame.Surface((self.size))
                
                # Checks if the position of a square is odd or even and colours it based on that
                if (gx % 2) == 0 and (gy % 2) == 1:
                    self.image.fill(color.c1)
                if (gx % 2) == 1 and (gy % 2) == 1:
                    self.image.fill(color.c2)
                if (gx % 2) == 0 and (gy % 2) == 0:
                    self.image.fill(color.c3)
                if (gx % 2) == 1 and (gy % 2) == 0:
                    self.image.fill(color.c4)
                    
                self.width, self.height = self.image.get_width(), self.image.get_height()
                self.rect = self.image.get_rect()            
                self.rect.x = gx*self.size[0]
                self.rect.y = gy*self.size[1]
                
                self.list_rect_x.append(self.rect.x)
                self.list_rect_y.append(self.rect.y)
                
                self.screen.blit(self.image,
                                 (self.rect.x+self.grid_paddingx, self.rect.y+self.grid_paddingy))       
        
        self.block_pos = [self.list_rect_x, self.list_rect_y]
