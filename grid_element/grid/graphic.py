import pygame

class grid(object):
    def __init__(
        self,
        to_surface,
        x:float,
        y:float,
        grid_size:tuple = (int,int)
    ):
        # positional args
        self.x = x
        self.y = y
        
        surf = pygame.Surface(grid_size)
        surf.fill(0,0,0)
        to_surface.blit(surf, (x,y))