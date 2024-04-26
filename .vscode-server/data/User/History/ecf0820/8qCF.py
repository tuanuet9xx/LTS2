import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
gray= (150,150,150)

while True:
    screen.fill(gray)
    for event in pygame.event.get():
        pass
    pygame.display.flip()