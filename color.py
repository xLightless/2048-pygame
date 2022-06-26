import random

def rgb():
    r = random.randint(0, 256)
    g = random.randint(0, 256)
    b = random.randint(0, 256)
    return tuple((r,g,b))

class Colors:
    PINK = (255, 100, 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    PURPLE = (88, 34, 161)
    MAGENTA = (120, 17, 160)
    ORANGE = (186, 137, 21)
    GRAY = (174, 163, 176)
    OLD_LAVENDER = (130, 112, 129)
    RANDOM_COLOR = rgb()
    
    background_color = (190,158,217)
    border_color = (112,41,172)
    c1 = (140,83,188)
    c2 = (169,126,205)
    c3 = (190,158,217)
    c4 = (187,185,227)
