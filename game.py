import pygame

from color import Colors
from gfxdraw import Button, callback

color = Colors()

class Engine(object):
    """ Handles screen data in engine for modulation """
    def __init__(
        self,
        screen,
        screen_fps
    ):
        self.screen         = screen
        self.width          = screen.get_width()
        self.height         = screen.get_height()
        clock               = pygame.time.Clock()
        self.fps            = clock.get_fps()
        terminated          = False
        
        DASHBOARD           = False
        GAME_SCREEN         = False
        
        while not terminated:
            """ Keeps engine open """
            try: screen.fill(color.RANDOM_COLOR)
            except Exception: continue
            finally: screen.fill(color.RANDOM_COLOR)
            mousepos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminated = True
                    
                if event.type == pygame.VIDEORESIZE:
                    self.width = screen.get_width()
                    self.height = screen.get_height()
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        DASHBOARD = True
                
            if DASHBOARD == True:
                screen.fill(color.RANDOM_COLOR)
                RESTART_BUTTON = Button(screen, self.width/2 - 104, self.height/2 - 27.5, 'Restart!', color.WHITE, color.BLACK, padding_x=100, padding_y=20, border_radius=9)
                QUIT_BUTTON = Button(screen, self.width/2 + 110, self.height/2 - 27.5, 'Quit', color.WHITE, color.BLACK, padding_x=100, padding_y=20, border_radius=9)
                
                if self.is_over(RESTART_BUTTON.rect, mousepos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                RESTART_BUTTON.event = callback("this is a function that runs when pressing a button")
                                DASHBOARD = False
                elif self.is_over(QUIT_BUTTON.rect, mousepos):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            RESTART_BUTTON.event = callback("You have pressed the quit button, good bye!")
                            terminated = True
                    
            clock.tick(screen_fps)
            pygame.display.update()
            pygame.display.flip()
       
        pygame.quit()
    
    def is_over(self, rect, pos):
        return True if rect.collidepoint(pos[0], pos[1]) else False