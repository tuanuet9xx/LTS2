import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

GREY= (150,150,150)
WHITE= (255,255,255)
BLACK= ( 0,0,0)
running = True
while True:
    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, BLACK, (200,150,50,50))
    pygame.draw.rect(screen, WHITE, (300,190,50,50))
    pygame.draw.rect(screen, BLACK, (200,250,50,50))
    pygame.draw.rect(screen, WHITE, (300,150,50,50))
    pygame.draw.rect(screen, BLACK, (200,180,50,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:


                print ("TUAN")

    pygame.display.flip()

pygame.quite()


