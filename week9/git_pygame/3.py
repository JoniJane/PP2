import pygame
pygame.init()

WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("JoniJane_ball")
run = True

clock = pygame.time.Clock()

x, y = 0, 0
speed = 20

while run:
    screen.fill('White')
    circle = pygame.draw.circle(screen, 'Red', (x, y), 25)
    #circle = pygame.image.load('week7/images/red_ball.png')
    #screen.blit(circle, (x, y))
    x = max(50, min(x, WIDTH - 50))
    y = max(50, min(y, HEIGHT - 50))

    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= speed
            if event.key == pygame.K_RIGHT:
                x += speed
            if event.key == pygame.K_UP:
                y -= speed
            if event.key == pygame.K_DOWN:
                y += speed
    
    clock.tick(60)