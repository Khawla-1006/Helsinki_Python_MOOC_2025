# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640,480))

window.fill((0,0,0))

robot = pygame.image.load("robot.png")
w = robot.get_width()
# window.blit(robot,(50,120))

x=50
for i in range(10):
    window.blit(robot,(x,120))
    x+=w

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()