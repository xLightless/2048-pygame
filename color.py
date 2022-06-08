import random

r = random.randint(0, 256)
g = random.randint(0, 256)
b = random.randint(0, 256)

color_tuple = (r, g, b)

class Colors:
    PINK = (255, 100, 100)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RANDOM_COLOR = color_tuple