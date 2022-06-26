import pygame

from grid.graphic import grid

screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
FPS = 120

terminated = False
while not terminated:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    screen.fill((255,255,255))
    grid(screen,500,500,(120,120))
    pygame.display.update()
    
pygame.quit()