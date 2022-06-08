""" Manages different screens or menus """
import pygame

from gfxdraw import Button
from color import Colors

color = Colors()

class Dashboard(object):
    def __init__(
        self,
        screen
    ):
        screen.fill(color.WHITE)
        width = screen.get_width()
        height = screen.get_height()
        PLAY_BUTTON = Button(screen, width/2, height/2, 'Play game', color.WHITE, color.BLACK)