# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint,choice
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = randint(0,640)
x1 = randint(0,640)
x2 = randint(0,640)

y = 0
y_dir1 = randint(1,5)
x_dir1 = choice([1,-1])

y_dir2 = randint(1,5)
x_dir2 = choice([1,-1])

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    window.blit(robot, (x, y))
    window.blit(robot, (x1, y))
    window.blit(robot, (x2, y))

    pygame.display.flip()

    y += y_dir1
    if y >= 480 - robot.get_height() :
        y_dir1 = 0
        x+=x_dir1
        x1+=x_dir1
        x2+=x_dir2
    
    clock.tick(60)

