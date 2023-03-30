import pygame
pygame.init()

screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("JoniJane_mp3")

clock = pygame.time.Clock()

youngblood = 'week7/music/5-seconds-of-summer-youngblood.mp3'
baq = 'week7/music/dudeontheguitar_Jeltoksan_-_baq_(musmore.com).mp3'
twoSoon = 'week7/music/musicbossorg_keshi_-_2_soon_63081217.mp3'

pygame.mixer.music.load('week7/music/5-seconds-of-summer-youngblood.mp3')
myList = [youngblood, baq, twoSoon]
pygame.mixer.music.play(-1)

flPause = False
index = 0
run = True

while run:
    screen.fill('Purple')
    player = pygame.image.load('week7/images/player.png')
    screen.blit(player, (20, 20))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                index += 1
                if index == len(myList):
                    index = 0
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                index -= 1
                if index == -1:
                    index = len(myList)-1
                pygame.mixer.music.load(myList[index])
                pygame.mixer.music.play()

    clock.tick(20)

