import pygame
import datetime
pygame.init()

WIDHT, HEIGHT = 800, 800
x, y = WIDHT//2, HEIGHT//2
sc = pygame.display.set_mode((WIDHT, HEIGHT))
pygame.display.set_caption("Mickey JoniJane")

clock = pygame.time.Clock()

clocks = pygame.image.load("week7/images/clock.jpg")
back = clocks.get_rect(center = (WIDHT//2, HEIGHT//2))

mickey = pygame.image.load("week7/images/body.png")
leftHand = pygame.image.load("week7/images/left-hand.png")
rightHand = pygame.image.load("week7/images/right-hand.png")
mickeyRect = mickey.get_rect()

sc.blit(clocks, back)
sc.blit(mickey, (400, 200))
sc.blit(leftHand, (100, 320))
sc.blit(rightHand, (0, 0))
pygame.display.update()

run = True 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
    pygame.display.update()
    clock.tick(60)