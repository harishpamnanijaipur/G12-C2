

import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()
win = pygame.display.set_mode((500,500))
crashed = False

x = 50
y = 50
width = 40
height = 60



while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()
quit()    