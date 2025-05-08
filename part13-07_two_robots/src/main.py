# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640,480))

robot = pygame.image.load("robot.png")

x = 0
y = 0

x1 = 120
y1 = 120

speed = 1
speed1 = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    window.fill((0,0,0))
    window.blit(robot,(x,y))
    window.blit(robot,(x1,y1))
    pygame.display.flip()

    x += speed
    if speed > 0 and x + robot.get_width() >= 640:
        speed = -speed
    
    if speed < 0 and x <= 0:
        speed = -speed

    x1 += speed1 * 2
    if speed1 > 0 and x1 + robot.get_width() >= 640:
        speed1 = -speed1 
    
    if speed1 < 0 and x1 <= 0:
        speed1 = -speed1 
    
    clock.tick(60)