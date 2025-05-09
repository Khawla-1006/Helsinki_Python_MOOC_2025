import pygame
from random import randint

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
x = randint(0,width - robot.get_width())
y = randint(0,height - robot.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

            hit_x = mouse_x >= x and mouse_x <= x + robot.get_width()
            hit_y = mouse_y >= y and mouse_y <= y + robot.get_height() 

            if hit_x and hit_y:
                x = randint(0, width - robot.get_width())
                y = randint(0,height + robot.get_height())

        if event.type == pygame.QUIT:
            exit()
        
        window.fill((0, 0, 0))
        window.blit(robot, (x  , y))
        pygame.display.flip()