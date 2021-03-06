from screeninfo import get_monitors
import pygame

import game
from color import Colors

""" Gets information about the monitor screen """
display_size = ""
for item in str(get_monitors()):
    if item.isdigit():
        display_size += item
WIDTH, HEIGHT = (int(display_size[2:6]), int(display_size[6:10]))

""" Pygame management """
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH/2, HEIGHT/2), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE); pygame.display.set_caption("512/1024/2048 v1.0.0"); pygame.display.set_icon(pygame.image.load('icon.png'))
SCREEN_FPS = 120
MONITOR_SIZE = [WIDTH, HEIGHT]

if __name__ == '__main__':
    engine = game.Engine(SCREEN, SCREEN_FPS, MONITOR_SIZE)