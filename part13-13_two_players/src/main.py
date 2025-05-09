# WRITE YOUR SOLUTION HERE:
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 60
y = 20

x1 = 100
y1 = 150

to_right = False
to_left = False
up = False
down = False

to_right1 = False
to_left1 = False
up1 = False
down1 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                to_left = True
            if event.key == pygame.K_RIGHT :
                to_right = True
            if event.key == pygame.K_UP :
                up = True
            if event.key == pygame.K_DOWN :
                down = True
            if event.key == pygame.K_a:
                to_left1 = True
            if event.key == pygame.K_d:
                to_right1 = True
            if event.key == pygame.K_w:
                up1 = True
            if event.key == pygame.K_s:
                down1 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT :
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP :
                up = False
            if event.key == pygame.K_DOWN :
                down = False
            if event.key == pygame.K_a:
                to_left1 = False
            if  event.key == pygame.K_d:
                to_right1 = False
            if event.key == pygame.K_w:
                up1 = False
            if  event.key == pygame.K_s:
                down1 = False


            


        if event.type == pygame.QUIT:
            exit()

    if to_right:
        if x <= 640 - robot.get_width():
            x += 2
    if to_left:
        if x > 0 :
            x -= 2
    if up :
        if y > 0 :
            y -= 2
    if down :
        if y <= 480 - robot.get_height():
            y += 2

    if to_right1:
        if x1 <= 640 - robot.get_width():
            x1 += 2
    if to_left1:
        if x1 > 0:
            x1 -= 2
    if up1 :
        if y1 > 0:
            y1 -= 2
    if down1 :
        if y1 <= 480 - robot.get_height():
            y1 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    window.blit(robot,(x1,y1))
    pygame.display.flip()

    clock.tick(60)