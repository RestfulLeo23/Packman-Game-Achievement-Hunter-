import pygame
import sys
import glob
import random
from pygame.locals import *
#Screen Dimensions
h = 600
w = 800
#Game Initialization
pygame.init()
clock = pygame.time.Clock()
background = pygame.image.load("PakMan Stage.png")
backgroundRect = background.get_rect()
size = (width, height) = background.get_size()



class Michael:
    def __init__(self):
        self.x = size[0]
        self.y = size[1]
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani_left = glob.glob("Michael_Sprite\Michael_Left*.png")
        self.ani_right = glob.glob("Michael_Sprite\Michael_Right*.png")
        self.ani_up = glob.glob("Michael_Sprite\Michael_Back*.png")
        self.ani_down = glob.glob("Michael_Sprite\Michael_Forward*.png")
        self.ani_down.sort()
        self.ani_up.sort()
        self.ani_left.sort()
        self.ani_right.sort()
        self.ani_posx = 0
        self.ani_posy = 0
        self.ani_left_max = len(self.ani_left)-1
        self.ani_right_max = len(self.ani_right)-1
        self.ani_up_max = len(self.ani_up)-1
        self.ani_down_max = len(self.ani_down) -1
        self.img_left = pygame.image.load(self.ani_left[0])
        self.img_right = pygame.image.load(self.ani_right[0])
        self.img_up = pygame.image.load(self.ani_up[0])
        self.img_down = pygame.image.load(self.ani_down[0])
        self.update(0,0)

    def update(self, posx, posy):
        if posy < 0:
            self.ani_speed -= 1
            self.y += posy
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        elif posx < 0:
            self.ani_speed -= 1
            self.x += posx
            if self.ani_speed == 0:
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))
        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx
            if self.ani_speed == 0:
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        if self.x < size[0]-size[0]:
            self.x = 0
        if self.x > size[0]-40:
            self.x = size[0]-40
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        elif posy > 0:
            self.ani_speed -= 1
            self.y += posy
            if self.ani_speed == 0:
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))


class MichaelAI:
    def __init__(self):
        self.x = size[0]/2
        self.y = size[1]/4
        self.ani_speed_init = 10
        self.ani_speed = self.ani_speed_init
        self.ani_left = glob.glob("Michael_Sprite\Michael_Left*.png")
        self.ani_right = glob.glob("Michael_Sprite\Michael_Right*.png")
        self.ani_up = glob.glob("Michael_Sprite\Michael_Back*.png")
        self.ani_down = glob.glob("Michael_Sprite\Michael_Forward*.png")
        self.ani_down.sort()
        self.ani_up.sort()
        self.ani_left.sort()
        self.ani_right.sort()
        self.ani_posx = 0
        self.ani_posy = 0
        self.ani_left_max = len(self.ani_left)-1
        self.ani_right_max = len(self.ani_right)-1
        self.ani_up_max = len(self.ani_up)-1
        self.ani_down_max = len(self.ani_down) -1
        self.img_left = pygame.image.load(self.ani_left[0])
        self.img_right = pygame.image.load(self.ani_right[0])
        self.img_up = pygame.image.load(self.ani_up[0])
        self.img_down = pygame.image.load(self.ani_down[0])
        self.update(0,0)

    def update(self, posx, posy):
        if posy < 0:
            self.ani_speed -= 1
            self.y += posy
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        elif posx < 0:
            self.ani_speed -= 1
            self.x += posx
            if self.ani_speed == 0:
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))
        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx
            if self.ani_speed == 0:
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        if self.x < size[0]-size[0]:
            self.x = 0
        if self.x > size[0]-40:
            self.x = size[0]-40
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        elif posy > 0:
            self.ani_speed -= 1
            self.y += posy
            if self.ani_speed == 0:
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

question = True

while question == True:
    try:
        playerprofile = input("Which character would you like to play as? Michael\n Jack\n Geoff\n Gavin\n Ray\n Ryan\n")
        if playerprofile == "Michael":
            player1 = Michael()
            AImichael = MichaelAI()
            aiposx = 0
            aiposy = 0
            posx = 1
            posy = 1
            question = False
    except ValueError:
        print("Wrong Character.")


screen = pygame.display.set_mode(size)
pygame.display.set_caption("Testing")
myfont = pygame.font.SysFont("monospace", 24)
score = 0
scoretext = myfont.render("Score = "+str(score), 1, (255,79,0))
posset = (-2,2,-2,2,-2,2)


    
    
        
        
while 1:
    clock.tick(60)
    screen.blit(background, backgroundRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            posx = 2
            posy = 0
            aiposx = random.choice(posset)
            aiposy = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:
            posx = -2
            posy = 0
            aiposx = random.choice(posset)
            aiposy = 0
        elif event.type == KEYDOWN and event.key == K_UP:
            posy = -2
            posx = 0
            aiposx = 0
            aiposy = random.choice(posset)
        elif event.type == KEYDOWN and event.key == K_DOWN:
            posy = 2
            posx = 0
            aiposx = 0
            aiposy = random.choice(posset)

       
            

        
    
    player1.update(posx,posy)
    AImichael.update(aiposx,aiposy)
    screen.blit(scoretext, (0,0))            
            
    pygame.display.update()
