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
            x1 = random.randint(0, blocks)
            x2 = random.randint(0, blocks)
            if x1!=x2:
                terminated = True
                
            for _ in range(0, blocks):
                block_list.append(0)
            
            # Gets the length of block list and finds the XY values and sets them to 1, keeping the rest at 0.
            for item in range(len(block_list)):
                if item == x1:
                    block_list[item] = 1
                    self.x1 = item
                    
                if item == x2:
                    block_list[item] = 1
                    self.x2 = item

        self.positions = (x1,x2) # List position of starting points
        self.block_list = block_list
        self.screen = screen
        self.size = size
        self.border = border
        self.grid_border = 22
        
        # Used to get the size of the grid object
        self.grid_width = self.grid_x*self.size[0]+self.grid_border
        self.grid_height = self.grid_y*self.size[1]+self.grid_border
        
    def draw(self):
        # These will be used for drawing objects to grid array
        self.list_rect = []

        self.text = pygame.font.Font('PilotCommandExpanded-8MY4g.otf', int(self.size[0]/3.8-8))
        self.num_font = pygame.font.Font('PilotCommandExpanded-8MY4g.otf', int(self.size[0]/4-8))
        
        # Padding options for moving objects
        self.grid_paddingx = (((self.screen.get_width())-self.grid_x*self.size[0])/2)
        self.grid_paddingy = (((self.screen.get_height())-self.grid_y*self.size[1])/2)
        
        SCORE = self.text.render('Good luck player!', True, color.BLACK, None)
        SCORE_RECT = SCORE.get_rect()
        SCORE_RECT.center = (self.screen.get_width()/2, self.grid_paddingy/2)
        self.screen.blit(SCORE, SCORE_RECT)

        # Background border for the grid
        if self.border == True:
            self.background = pygame.Rect(self.grid_paddingx-(self.grid_border/2), self.grid_paddingy-(self.grid_border/2), 
                                      self.grid_x*self.size[0]+self.grid_border, self.grid_y*self.size[1]+self.grid_border)
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
                
                self.list_rect.append((self.rect.x, self.rect.y))                
                self.screen.blit(self.image,
                                (self.rect.x+self.grid_paddingx, self.rect.y+self.grid_paddingy))
                
                # f"{x if self.list_rect.index(x) == self.positions[0] else '1'}"
                num = self.num_font.render('1', True, color.BLACK, None)
                self.screen.blit(num, (self.grid_paddingx+self.rect.centerx-(num.get_width()/2), self.grid_paddingy+self.rect.centery-(num.get_height()/2)))        

class Tile(pygame.sprite.Sprite):
    def __init__(
        self,
        x,
        y
    ):
        super().__init__()
        
        self.font = pygame.font.Font('PilotCommandExpanded-8MY4g.otf', 32)