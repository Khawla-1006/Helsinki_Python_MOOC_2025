import pygame

pygame.init()

window = pygame.display.set_mode((640,480))

window.fill((0,0,0))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

j = 1
vertical= 40
horizental = 30

while j <= 10:
    for i in range(10):
        window.blit(robot,(horizental,vertical))
        horizental += width
    horizental = 30 + width/4 * j
    vertical = 40 + height/4 * j
    j += 1

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
