# Complete your game here


#GAME_EXPLANATION:

    #The player moves the robot to the left and right along the bottom of the screen.
    #Coins rain from the sky. The robot must collect these. points increase ++
    #Also monsters rain from the sky. The robot must avoid these. if monster hits the robot points decrease --
    # hide from the monsters through the door! but it costs 10 pts!
    #try to score as much as you can ! if pts < -1000 the game is OVER ! you lose!
    #enjoy!!

import pygame
from random import randint

class CoinsRain:
    def __init__(self):
        pygame.init()

        self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("COINS RAINFALL")
        self.game_font = pygame.font.SysFont("Arial",24)
        self.exit_font = pygame.font.SysFont("Arial",90)

        self.robot = pygame.image.load("robot.png")
        self.coin = pygame.image.load("coin.png")
        self.door = pygame.image.load("door.png") #to escape from monsters!
        self.monster = pygame.image.load("monster.png")

        self.robot_x = 0
        self.robot_y = 480 - self.robot.get_height()
        self.robot_to_left = False
        self.robot_to_right = False
        self.pts = 0
        # number of coins (the same coins are reused)
        self.number = 8

        self.coins = []
        for i in range(self.number):
            # causes the new random start position to be drawn immediately
            self.coins.append([-1000,self.height])

        self.monsters = []
        for i in range(self.number*3): #more monsters than coins lol!
            self.monsters.append([-1000,self.height])

        self.clock = pygame.time.Clock()

        self.main_loop()
    
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_screen()
        
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.robot_to_left = True
                if event.key == pygame.K_RIGHT:
                    self.robot_to_right = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.robot_to_left = False
                if event.key == pygame.K_RIGHT:
                    self.robot_to_right = False

        if self.robot_to_right :
            self.robot_x += 10
        if self.robot_to_left and self.robot_x > 0:
            self.robot_x -= 10
    
    def draw_screen(self):
        self.screen.fill((214,255,249))

        if self.pts <= -1000:
            exit_text = self.game_font.render("GAME OVER!",True,(255,0,0))
            self.screen.blit(exit_text,(200,200))
        # the coin falls downwards
        for i in range(self.number):
            self.coins[i][1] += 1
            #collect coins earn points
            # if self.coins[i][1] + self.robot.get_height() >= self.height:
            #     self.pts += 1 #do not seem to work:/
            if self.coins[i][0] < -self.robot.get_width() or self.coins[i][0] > self.width:
                self.coins[i][0] = randint(0,self.width-self.coin.get_width())
                self.coins[i][1] = -randint(100,1000)

        # the monsters falls downwards
        for i in range(self.number):
            self.monsters[i][1] += 1
            #hit a monster loose points
            # if self.monsters[i][1] + self.robot.get_height() >= self.height:
                # self.pts -= 1 #do not seem to work:/
            if self.monsters[i][0] < -self.monster.get_width() or self.monsters[i][0] > self.width:
                self.monsters[i][0] = randint(0,self.width - self.monster.get_width())
                self.monsters[i][1] = - randint(100,1000)

        #hide through the door but it costs points !
        if self.robot_x >= self.width - self.door.get_width():
            self.pts -= 10
        

        for i in range(self.number):
            self.screen.blit(self.coin, (self.coins[i][0], self.coins[i][1]))
 


        for i in range(self.number * 3):
            self.screen.blit(self.monster,(self.monsters[i][0],self.monsters[i][1]))


        self.screen.blit(self.robot,(self.robot_x,self.robot_y))
        self.screen.blit(self.door,(645 - self.door.get_width(),485 - self.door.get_height()))
        game_text = self.game_font.render("Points:" + str(self.pts),True,(255,0,0))
        self.screen.blit(game_text,(25,120))
        pygame.display.flip()    
        self.clock.tick(60)

if __name__ == "__main__":
    CoinsRain()