import pygame
pygame.init()

screen = pygame.display.set_mode((500,500))

GREY= (150,150,150)
WHITE= (255,255,255)
BLACK= ( 0,0,0)
running = True
font= pygame.font.SysFont('san', 50)
text_1= font.render('+', True, BLACK)
while True:
    screen.fill(GREY)
    pygame.draw.rect(screen, WHITE, (100,50,50,50))
    pygame.draw.rect(screen, WHITE, (200,150,50,50))
    pygame.draw.rect(screen, WHITE, (300,190,50,50))
    pygame.draw.rect(screen, WHITE, (200,250,50,50))
    pygame.draw.rect(screen, WHITE, (300,150,50,50))
    pygame.draw.rect(screen, WHITE, (200,180,50,50))
    pygame.draw.rect(screen, WHITE, (200,180,50,50))

    screen.split (text_1, (100,50))

    screen.split (text_1, (100,200))
    screen.split (text_1, (200,50))
    screen.split (text_1, (200,200))
    screen.split (text_1, (300,50))
    screen.split (text_1, (300,200))

    pygame.draw.rect(screen, BLACK, (50,180,50,50))
    pygame.draw.rect(screen, WHITE, (60,180,50,50))
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:


                print ("TUAN")

    pygame.display.flip()

pygame.quite()


