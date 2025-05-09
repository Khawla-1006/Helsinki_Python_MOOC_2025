# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))

ball = pygame.image.load("ball.png")

x = 240
y = 180

x_dir = 1
y_dir = 1

clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill((0,0,0))
    screen.blit(ball,(x,y))
    pygame.display.flip()

    x += x_dir
    y += y_dir

    if y >= 480 - ball.get_height() :
        y_dir = -1
    if y < 0:
        y_dir = 1
    if x >= 640 - ball.get_width():
        x_dir = -1
    if x < 0:
        x_dir = 1
     

    clock.tick(60)