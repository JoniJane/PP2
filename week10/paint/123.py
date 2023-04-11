import pygame
pygame.init()

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

W, H = 400, 600
sc = pygame.display.set_mode((W, H))
sc.fill(WHITE)
pygame.display.set_caption("PAINT")

color = BLACK
shape = 'line'
width = 10
startPos, endPos = 0, 0
run = True

while run:
    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()
        ctrl_pressed = pressed[pygame.K_RCTRL] or pressed[pygame.K_LCTRL]
    
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if pressed[pygame.K_DOWN] and width > 1:
                width -= 1
            if pressed[pygame.K_UP]:
                width += 1
            if pressed[pygame.K_b]:
                color = BLUE
            if pressed[pygame.K_r]:
                color = RED
            if pressed[pygame.K_g]:
                color = GREEN
            if ctrl_pressed and pressed[pygame.K_l]:
                shape = 'line'
            if ctrl_pressed and pressed[pygame.K_e]:
                shape = 'eraser'
            if ctrl_pressed and pressed[pygame.K_c]:
                shape = 'circle'
            if ctrl_pressed and pressed[pygame.K_r]:
                shape = 'rectangle'
            

        if shape == 'line' or shape == 'eraser':
            if event.type == pygame.MOUSEBUTTONDOWN:
                startPos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEMOTION:
                endPos = pygame.mouse.get_pos()
                if startPos:
                    if shape == 'line':
                        pygame.draw.line(sc, color, startPos, endPos, width)
                    if shape == 'eraser':
                        pygame.draw.line(sc, WHITE, startPos, endPos, width)
                    startPos = endPos
            if event.type == pygame.MOUSEBUTTONUP:
                startPos = None
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                startPos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                endPos = pygame.mouse.get_pos()
                if shape == 'rectangle':
                    x = min(startPos[0], endPos[0])
                    y = min(startPos[1], endPos[1])
                    lx = abs(startPos[0]-endPos[0])
                    ly = abs(startPos[1]-endPos[1])
                    pygame.draw.rect(sc, color, (x, y, lx, ly), width)
                if shape == 'circle':
                    x = (startPos[0]+endPos[0])/2
                    y = (startPos[1]+endPos[1])/2
                    rx = abs(startPos[0]-endPos[0])/2
                    ry = abs(startPos[1]-endPos[1])/2
                    r = (rx + ry)/2
                    pygame.draw.circle(sc, color, (x, y), r, width)
                
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
