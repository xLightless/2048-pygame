import pygame
import os

from color import Colors
from gfxdraw import Button
from game_logic import GRID_ARRAY

color   = Colors()

class Engine(object):
    """ Handles screen data in engine for modulation """
    def __init__(
        self,
        screen,
        screen_fps,
        monitor_size
    ):
        self.screen         = screen
        fullscreen          = False
        self.width          = screen.get_width()
        self.height         = screen.get_height()
        clock               = pygame.time.Clock()
        self.fps            = clock.get_fps()
        terminated          = False
        DASHBOARD           = False
        GRID_X              = 4
        GRID_Y              = 4
        SIZE                = (128, 128)
        sq                  = GRID_ARRAY(screen, SIZE, GRID_X, GRID_Y)
        
        while not terminated:
            """ Keeps engine open """
            screen.fill(color.background_color)
            mousepos = pygame.mouse.get_pos()

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminated = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        DASHBOARD = True
                    elif event.key == pygame.K_F11:
                        fullscreen = not fullscreen
                        if fullscreen:
                            screen = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                        else:
                            screen = pygame.display.set_mode((monitor_size[0]/2, monitor_size[1]/2), pygame.RESIZABLE)
                            
            if not DASHBOARD:
                pygame.display.set_caption("GAME SCREEN")
                sq.draw()
           
            if DASHBOARD == True:
                screen.fill(color.RANDOM_COLOR)
                pygame.display.set_caption("DASHBOARD")
                RESTART_BUTTON = Button(screen, screen.get_width()/2 - 104, screen.get_height()/2 - 27.5, 'Restart!', color.WHITE, color.BLACK, padding_x=80, padding_y=10, border_radius=7)
                QUIT_BUTTON = Button(screen, screen.get_width()/2 + 110, screen.get_height()/2 - 27.5, 'Quit', color.WHITE, color.BLACK, padding_x=80, padding_y=10, border_radius=7, hide=False)
                RELOAD_BUTTON = Button(screen, 10, 10, 'Reload', color.WHITE, color.BLACK, padding_x=80, padding_y=10, border_radius=7)
                
                try:
                    if self.is_over(RESTART_BUTTON.rect, mousepos):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                RESTART_BUTTON.event = None
                                DASHBOARD = False
                                
                    elif self.is_over(QUIT_BUTTON.rect, mousepos):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                RESTART_BUTTON.event = print("You have pressed the quit button, good bye!")
                                terminated = True
                                
                    elif self.is_over(RELOAD_BUTTON.rect, mousepos):
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                terminated = True
                                pygame.display.quit()
                                RELOAD_BUTTON.event = os.system(f'py main.py')

                except pygame.error:
                    pass
                    
            clock.tick(screen_fps)
            pygame.display.update()
            pygame.display.flip()
            
    def is_over(self, rect, pos):
            """ checks if mouse is over a rect position """
            return True if rect.collidepoint(pos[0], pos[1]) else False
    