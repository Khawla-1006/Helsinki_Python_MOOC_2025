import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0]-robot.get_width()/2
            target_y = event.pos[1]-robot.get_height()/2

        if event.type == pygame.QUIT:
            exit(0)

    if robot_x > target_x:
        robot_x -= 1
    if robot_x < target_x:
        robot_x += 1
    if robot_y > target_y:
        robot_y -= 1
    if robot_y < target_y:
        robot_y += 1

    window.fill((0, 0, 0))
    window.blit(robot, (target_x, target_y))
    pygame.display.flip()

    clock.tick(60)