import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))
GREY= (150,150,150)

while True:
    screen.fill(GREY)
    for event in pygame.event.get():
        pass
    pygame.display.flip()

pygame.quite()


    