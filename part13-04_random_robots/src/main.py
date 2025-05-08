# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint


pygame.init()

window = pygame.display.set_mode((640,480))

window.fill((0,0,0))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

for i in range(1000):
    window.blit(robot,((randint(0,640-width),randint(0,480-height))))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()