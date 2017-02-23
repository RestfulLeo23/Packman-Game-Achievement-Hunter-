import pygame, sys, glob, random
from pygame import *

#Game Initialization
pygame.init()
clock = pygame.time.Clock()
background = pygame.image.load("PakMan Stage.png")
backgroundRect = background.get_rect()
size = (width, height) = background.get_size()


#Base for all of my Classes
#Classes were based off of a tutorial code that I have modified to work for me
#
#
#########################################################################################################
#                             Base Code for animation sequence is as follows.                           #
#Citation: http://stackoverflow.com/questions/14044147/animated-sprite-from-few-images User:Michael0x2a # 
#########################################################################################################
##  class player:                                                                                      ##
##      def _init_(self):                                                                              ##
##          self.x = 200                                                                               ##
##          self.y = 300                                                                               ##
##          self.ani_speed_init = 10                                                                   ##
##          self.ani_speed = self.ani_speed_init                                                       ##
##          self.ani = glob.glob("walk/doom_w*.png")                                                   ##
##          self.ani.sort()                                                                            ##
##          self.ani_pos = 0                                                                           ##
##          self.ani_max = len(self.ani) - 1                                                           ##
##          self.img = pygame.image.load(self.ani[0])                                                  ##
##          self.update(0)                                                                             ##
##      def update(self,pos):                                                                          ##
##          if pos != 0:                                                                               ##
##              self.ani_speed -=1                                                                     ##
##              self.x+=pos                                                                            ##
##              if self.ani_speed == 0:                                                                ##
##                  self.img = pygame.image.load(self.ani[self.ani_pos])                               ##
##                  self.ani_speed = self.ani_speed_init                                               ##
##                  if self.ani_pos == self.ani_max:                                                   ##
##                      self.ani_pos = 0                                                               ##
##                  else:                                                                              ##
##                      self.ani_pos += 1                                                              ##
##          screen.blit(self.img,(self.x,self.y))                                                      ##
##########################################################################################################
##########################################################################################################



################################################
##                                            ##
#                Player Classes                #
# Code was designed based on several different #
#    versions of player classes found online   #
##                                            ##
################################################



#1st Character class
class Michael:
    #Initializes all variables for Michael
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Michael_Sprite\Michael_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Michael_Sprite\Michael_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Michael_Sprite\Michael_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Michael_Sprite\Michael_Forward*.png")  #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Michael

    #Defines the function for moving michael based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends michael in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ####################
            self.ani_speed -= 1                                                     # Moves Michael Up #
            self.y += posy                                                          ####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends michael in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ######################
            self.x += posx                                                          # Moves Michael Left #
            if self.ani_speed == 0:                                                 ######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #######################
            if self.ani_speed == 0:                                                 # Moves Michael Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #######################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ######################
            self.y += posy                                                          # Moves Michael Down #
            if self.ani_speed == 0:                                                 ######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))
        

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #  Checks to see if michael is making contact with the wall   #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates
        




#2nd Character class
class Jack:
    #Initializes all variables for Jack
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Jack_Sprite\Jack_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Jack_Sprite\Jack_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Jack_Sprite\Jack_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Jack_Sprite\Jack_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Jack

    #Defines the function for moving Jack based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Jack in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                #################
            self.ani_speed -= 1                                                     # Moves Jack Up #
            self.y += posy                                                          #################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Jack in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ###################
            self.x += posx                                                          # Moves Jack Left #
            if self.ani_speed == 0:                                                 ###################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          ####################
            if self.ani_speed == 0:                                                 # Moves Jack Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   ####################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ###################
            self.y += posy                                                          # Moves Jack Down #
            if self.ani_speed == 0:                                                 ###################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #    Checks to see if Jack is making contact with the wall    #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates


#3rd Character class
class Geoff:
    #Initializes all variables for Geoff
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Geoff_ Sprite\Geoff_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Geoff_ Sprite\Geoff_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Geoff_ Sprite\Geoff_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Geoff_ Sprite\Geoff_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Geoff

    #Defines the function for moving Jack based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Geoff in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ##################
            self.ani_speed -= 1                                                     # Moves Geoff Up #
            self.y += posy                                                          ##################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Geoff in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ####################
            self.x += posx                                                          # Moves Geoff Left #
            if self.ani_speed == 0:                                                 ####################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #####################
            if self.ani_speed == 0:                                                 # Moves Geoff Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #####################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ####################
            self.y += posy                                                          # Moves Geoff Down #
            if self.ani_speed == 0:                                                 ####################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #    Checks to see if Geoff is making contact with the wall   #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates


#4th Character class
class Ryan:
    #Initializes all variables for Ryan
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Ryan_Sprite\Ryan_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Ryan_Sprite\Ryan_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Ryan_Sprite\Ryan_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Ryan_Sprite\Ryan_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Ryan

    #Defines the function for moving Jack based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Ryan in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                #################
            self.ani_speed -= 1                                                     # Moves Ryan Up #
            self.y += posy                                                          #################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Ryan in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ###################
            self.x += posx                                                          # Moves Ryan Left #
            if self.ani_speed == 0:                                                 ###################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          ####################
            if self.ani_speed == 0:                                                 # Moves Ryan Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   ####################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ###################
            self.y += posy                                                          # Moves Ryan Down #
            if self.ani_speed == 0:                                                 ###################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #    Checks to see if Ryan is making contact with the wall    #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates

#5th Character class
class Ray:
    #Initializes all variables for Ray
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Ray_Sprite\Ray_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Ray_Sprite\Ray_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Ray_Sprite\Ray_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Ray_Sprite\Ray_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Ray

    #Defines the function for moving Ray based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Ray in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ################
            self.ani_speed -= 1                                                     # Moves Ray Up #
            self.y += posy                                                          ################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Ray in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ##################
            self.x += posx                                                          # Moves Ray Left #
            if self.ani_speed == 0:                                                 ##################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          ###################
            if self.ani_speed == 0:                                                 # Moves Ray Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   ###################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ##################
            self.y += posy                                                          # Moves Ray Down #
            if self.ani_speed == 0:                                                 ##################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #    Checks to see if Ray is making contact with the wall     #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates



#6th Character class
class Gavin:
    #Initializes all variables for Gavin
    def __init__(self):
        self.x = size[0]-400#x position
        self.y = size[1]-400#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Gavin_Sprite\Gavin_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Gavin_Sprite\Gavin_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Gavin_Sprite\Gavin_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Gavin_Sprite\Gavin_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Gavin

    #Defines the function for moving Gavin based on which key is pressed
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Gavin in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ##################
            self.ani_speed -= 1                                                     # Moves Gavin Up #
            self.y += posy                                                          ##################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Ray in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ####################
            self.x += posx                                                          # Moves Gavin Left #
            if self.ani_speed == 0:                                                 ####################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #####################
            if self.ani_speed == 0:                                                 # Moves Gavin Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #####################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ####################
            self.y += posy                                                          # Moves Gavin Down #
            if self.ani_speed == 0:                                                 ####################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                        ###############################################################
            self.x = 0                                      #    Checks to see if Gavin is making contact with the wall   #
        if self.x > size[0]-40:                             # If he is, then it stops him and places him where he stopped #
            self.x = size[0]-40                             ###############################################################
        if self.y < size[1]-size[1]:
            self.y = 0
        if self.y > size[1]-130:
            self.y = size[1]-130

        player_coordinates = (self.x,self.y)
        
        
        return player_coordinates

####################################
##                                ##
#            AI Classes            #
##                                ##
####################################

#1st AI Character class
class MichaelAI:
    #Initializes all variables for Michael
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Michael_Sprite\Michael_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Michael_Sprite\Michael_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Michael_Sprite\Michael_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Michael_Sprite\Michael_Forward*.png")  #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Michael

    #Defines the function for moving michael based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends michael in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ####################
            self.ani_speed -= 1                                                     # Moves Michael Up #
            self.y += posy                                                          ####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends michael in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ######################
            self.x += posx                                                          # Moves Michael Left #
            if self.ani_speed == 0:                                                 ######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #######################
            if self.ani_speed == 0:                                                 # Moves Michael Right #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #######################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ######################
            self.y += posy                                                          # Moves Michael Down #
            if self.ani_speed == 0:                                                 ######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Michael hits the# 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0
        
        ai_coordinates = (self.x,self.y)
        return ai_coordinates


#2nd AI Character class
class JackAI:
    #Initializes all variables for Jack
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Jack_Sprite\Jack_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Jack_Sprite\Jack_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Jack_Sprite\Jack_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Jack_Sprite\Jack_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Jack

    #Defines the function for moving Jack based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Jack in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                #####################
            self.ani_speed -= 1                                                     #   Moves Jack Up   #
            self.y += posy                                                          #####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Jack in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     #######################
            self.x += posx                                                          #   Moves Jack Left   #
            if self.ani_speed == 0:                                                 #######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          ########################
            if self.ani_speed == 0:                                                 #   Moves Jack Right   #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   ########################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     #######################
            self.y += posy                                                          #   Moves Jack Down   #
            if self.ani_speed == 0:                                                 #######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Jack hits the   # 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0

        ai_coordinates = (self.x,self.y)
        return ai_coordinates

#3rd AI Character class
class GeoffAI:
    #Initializes all variables for Geoff
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Geoff_ Sprite\Geoff_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Geoff_ Sprite\Geoff_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Geoff_ Sprite\Geoff_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Geoff_ Sprite\Geoff_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Geoff

    #Defines the function for moving Geoff based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Geoff in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ####################
            self.ani_speed -= 1                                                     #  Moves Geoff Up  #
            self.y += posy                                                          ####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Geoff in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ######################
            self.x += posx                                                          #  Moves Geoff Left  #
            if self.ani_speed == 0:                                                 ######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #######################
            if self.ani_speed == 0:                                                 #  Moves Geoff Right  #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #######################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ######################
            self.y += posy                                                          #  Moves Geoff Down  #
            if self.ani_speed == 0:                                                 ######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Geoff hits the  # 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0

        ai_coordinates = (self.x,self.y)
        return ai_coordinates


#4th AI Character class
class RyanAI:
    #Initializes all variables for Ryan
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Ryan_Sprite\Ryan_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Ryan_Sprite\Ryan_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Ryan_Sprite\Ryan_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Ryan_Sprite\Ryan_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Ryan

    #Defines the function for moving Ryan based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Ryan in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                #####################
            self.ani_speed -= 1                                                     #   Moves Ryan Up   #
            self.y += posy                                                          #####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Ryan in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     #######################
            self.x += posx                                                          #   Moves Ryan Left   #
            if self.ani_speed == 0:                                                 #######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          ########################
            if self.ani_speed == 0:                                                 #   Moves Ryan Right   #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   ########################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     #######################
            self.y += posy                                                          #   Moves Ryan Down   #
            if self.ani_speed == 0:                                                 #######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Ryan hits the   # 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0

        ai_coordinates = (self.x,self.y)
        return ai_coordinates

#5th AI Character class
class RayAI:
    #Initializes all variables for Ray
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Ray_Sprite\Ray_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Ray_Sprite\Ray_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Ray_Sprite\Ray_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Ray_Sprite\Ray_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Ray

    #Defines the function for moving Ray based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Ray in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ####################
            self.ani_speed -= 1                                                     #   Moves Ray Up   #
            self.y += posy                                                          ####################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Ray in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ######################
            self.x += posx                                                          #   Moves Ray Left   #
            if self.ani_speed == 0:                                                 ######################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #######################
            if self.ani_speed == 0:                                                 #   Moves Ray Right   #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #######################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ######################
            self.y += posy                                                          #   Moves Ray Down   #
            if self.ani_speed == 0:                                                 ######################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Ray hits the    # 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0

        ai_coordinates = (self.x,self.y)
        return ai_coordinates


#6th AI Character class
class GavinAI:
    #Initializes all variables for Gavin
    def __init__(self):
        self.x = size[0]/2#x position
        self.y = size[1]/4#y position
        self.ani_speed_init = 10#Initial Speed
        self.ani_speed = self.ani_speed_init#Setting speed equal to initial
        self.ani_left = glob.glob("Gavin_Sprite\Gavin_Left*.png")     #Loading left walking animations into a list
        self.ani_right = glob.glob("Gavin_Sprite\Gavin_Right*.png")   #Loading right walking animations into a list
        self.ani_up = glob.glob("Gavin_Sprite\Gavin_Back*.png")       #Loading Back walking animations into a list
        self.ani_down = glob.glob("Gavin_Sprite\Gavin_Front*.png")    #Loading Forward walking animations into a list
        self.ani_down.sort()   #Sorting the Forward animations into numerical order so they animate properly
        self.ani_up.sort()     #Sorting the Backward animations into numerical order so they animate properly
        self.ani_left.sort()   #Sorting the Left animations into numerical order so they animate properly
        self.ani_right.sort()  #Sorting the Right animations into numerical order so they animate proplery
        self.ani_posx = 0      #Initializing the x pos for the key inputs
        self.ani_posy = 0      #Initializing the y pos for the key inputs
        self.ani_left_max = len(self.ani_left)-1    #Setting the maximum numbers of times the list of Left walking animations goes before it loops
        self.ani_right_max = len(self.ani_right)-1  #Setting the maximum numbers of times the list of Right walking animations goes before it loops
        self.ani_up_max = len(self.ani_up)-1        #Setting the maximum numbers of times the list of Backward walking animations goes before it loops
        self.ani_down_max = len(self.ani_down) -1   #Setting the maximum numbers of times the list of Forward walking animations goes before it loops
        self.img_left = pygame.image.load(self.ani_left[0])    #Setting the left walking variable equal to the list of left walking animation png's
        self.img_right = pygame.image.load(self.ani_right[0])  #Setting the right walking variable equal to the list of right walking animation png's
        self.img_up = pygame.image.load(self.ani_up[0])        #Setting the backward walking variable equal to the list of backward walking animation png's
        self.img_down = pygame.image.load(self.ani_down[0])    #Setting the forward walking variable equal to the list of forward walking animation png's 
        self.update(0,0)   #Initializes Gavin

    #Defines the function for moving Gavin based on a random selection of numbers which is dependent upon which character the user selects to play as. The Key presses by the user then dictate which random sequence generates for the axis the user selects to move
    def update(self, posx, posy):
        #Checks which keys is pressed and then sends Gavin in the direction based on the key input for the y axis by the user
        if posy < 0:                                                                ######################
            self.ani_speed -= 1                                                     #   Moves Gavin Up   #
            self.y += posy                                                          ######################
            if self.ani_speed == 0:
                self.img_up = pygame.image.load(self.ani_up[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_up_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_up,(self.x,self.y))
        #Checks which keys is pressed and then sends Gavin in the direction based on the key input for the x axis by the user
        elif posx < 0:
            self.ani_speed -= 1                                                     ########################
            self.x += posx                                                          #   Moves Gavin Left   #
            if self.ani_speed == 0:                                                 ########################
                self.img_left = pygame.image.load(self.ani_left[self.ani_posx])
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_left_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_left,(self.x,self.y))

        elif posx > 0:
            self.ani_speed -= 1
            self.x += posx                                                          #########################
            if self.ani_speed == 0:                                                 #   Moves Gavin Right   #
                self.img_right = pygame.image.load(self.ani_right[self.ani_posx])   #########################
                self.ani_speed = self.ani_speed_init
                if self.ani_posx == self.ani_right_max:
                    self.ani_posx = 0
                else:
                    self.ani_posx+=1
            screen.blit(self.img_right,(self.x,self.y))
        
        elif posy > 0:
            self.ani_speed -= 1                                                     ########################
            self.y += posy                                                          #   Moves Gavin Down   #
            if self.ani_speed == 0:                                                 ########################
                self.img_down = pygame.image.load(self.ani_down[self.ani_posy])
                self.ani_speed = self.ani_speed_init
                if self.ani_posy == self.ani_down_max:
                    self.ani_posy = 0
                else:
                    self.ani_posy+=1
            screen.blit(self.img_down,(self.x,self.y))

        if self.x < size[0]-size[0]:                                                ########################
            self.x = size[0]-40                                                     # When Gavin hits the  # 
        if self.x > size[0]-40:                                                     # wall, he reflects to #
            self.x = 0                                                              # the opposite wall.   #
        if self.y < size[1]-size[1]:                                                ########################
            self.y = size[1]-130                                                    
        if self.y > size[1]-130:                                                    
            self.y = 0

        ai_coordinates = (self.x,self.y)
        return ai_coordinates



# Ball object that the player must collect without getting tagged by the AI       
class Ball:
    def __init__(self):#Initializes the Ball into the game
        self.x = 0
        self.y = 0
        self.update(0,0)
    def update(self,sizex,sizey):#Defines where the ball goes on the background
        ball_x_position = sizex
        ball_y_position = sizey

        x1 = ball_x_position - 50
        y1 = ball_y_position - 50
        x2 = ball_x_position - 50
        y2 = ball_y_position - 750
        x3 = ball_x_position - 750
        y3 = ball_y_position - 750
        x4 = ball_x_position - 750
        y4 = ball_y_position - 50
        ball_coordinates = [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]
            

        return ball_coordinates
            
        
        
    
            
    


#Initializes all of the player's and AI's coordinates on the background into seperate tuples
question = True
player_tuple = ()
ai_tuple = ()
ai2_tuple = ()
ai3_tuple = ()
ai4_tuple = ()
ai5_tuple = ()
ball_tuple = ()

print('Welcome to the Achievement Hunter Version of Pacman!')
print('')
print('The objective is simple, collect enough points to win. If the other lads and gents hit you, they deduct points.')
print('')
print('If you loose all of your points to the lads or the gents, you loose! If you get 500, you win!')
print('')
print('WARNING')
print('Every time a lad or gent makes contact with you, they deduct points until you stop touching them')
print('Every time you make contact with a ball you collect points however, be aware that the ai will suddenly change direction when you press certain keys. They will not always go on the same axis as you.')
print('')
print('RULES')
print('You can not sit on top of a ball and collect points until you hit 500. You must constantly move around')
print('Good Luck!')
print('')
#Input for user character selection
while question == True:
    #Checks to make sure user inputs correct character and also to make sure input is in string format
    try:
        playerprofile = input("Which character would you like to play as?\n Michael\n Jack\n Geoff\n Gavin\n Ray\n Ryan\n")
        #If user selects Michael, all other characters are assigned an AI profile
        #AI and user positions are initialized
        player = playerprofile.capitalize()
        if player == "Michael":
            player1 = Michael()
            AI1 = JackAI()
            AI2 = GeoffAI()
            AI3 = RyanAI()
            AI4 = RayAI()
            AI5 = GavinAI()
            ball = Ball()
            ai1posx = 1
            ai1posy = 0
            ai2posx = -1
            ai2posy = 0
            ai3posx = 0
            ai3posy = 1
            ai4posx = 0
            ai4posy = -1
            ai5posx = -1
            ai5posy = -1
            posx = -1
            posy = 1
            question = False
        #If user selects Jack, all other characters are assigned an AI profile
        #AI and user positions are initialized
        elif player == "Jack":
            player1 = Jack()
            AI1 = MichaelAI()
            AI2 = RyanAI()
            AI3 = GeoffAI()
            AI4 = RayAI()
            AI5 = GavinAI()
            ball = Ball()
            ai1posx = 0
            ai1posy = 1
            ai2posx = 0
            ai2posy = -1
            ai3posx = 1
            ai3posy = 0
            ai4posx = -1
            ai4posy = 0
            ai5posx = -1
            ai5posy = -1
            posx = 1
            posy = 1
            question = False
        #If user selects Geoff, all other characters are assigned an AI profile
        #AI and user positions are initialized
        elif player == "Geoff":
            player1 = Geoff()
            AI1 = JackAI()
            AI2 = MichaelAI()
            AI3 = RyanAI()
            AI4 = GavinAI()
            AI5 = RayAI()
            ball = Ball()
            ai1posx = 0
            ai1posy = 1
            ai2posx = 0
            ai2posy = -1
            ai3posx = 1
            ai3posy = 0
            ai4posx = -1
            ai4posy = 0
            ai5posx = -1
            ai5posy = -1
            posx = 1
            posy = 1
            question = False
        #If user selects Ryan, all other characters are assigned an AI profile
        #AI and user positions are initialized
        elif player == "Ryan":
            player1 = Ryan()
            AI1 = GeoffAI()
            AI2 = JackAI()
            AI3 = MichaelAI()
            AI4 = RayAI()
            AI5 = GavinAI()
            ball = Ball()
            ai1posx = 1
            ai1posy = 1
            ai2posx = 0
            ai2posy = 1
            ai3posx = 1
            ai3posy = 0
            ai4posx = 1
            ai4posy = 0
            ai5posx = 1
            ai5posy = 1
            posx = 1
            posy = 1
            question = False
        #If user selects Ray, all other characters are assigned an AI profile
        #AI and user positions are initialized
        elif player == "Ray":
            player1 = Ray()
            AI1 = GavinAI()
            AI2 = MichaelAI()
            AI3 = RyanAI()
            AI4 = GeoffAI()
            AI5 = JackAI()
            ball = Ball()
            ai1posx = -1
            ai1posy = -1
            ai2posx = 0
            ai2posy = 1
            ai3posx = -1
            ai3posy = 0
            ai4posx = 1
            ai4posy = 0
            ai5posx = 1
            ai5posy = 1
            posx = 1
            posy = 1
            question = False
        #If user selects Gavin, all other characters are assigned an AI profile
        #AI and user positions are initialized
        elif player == "Gavin":
            player1 = Gavin()
            AI1 = RayAI()
            AI2 = MichaelAI()
            AI3 = RyanAI()
            AI4 = JackAI()
            AI5 = GeoffAI()
            ball = Ball()
            ai1posx = 0
            ai1posy = 1
            ai2posx = 0
            ai2posy = -1
            ai3posx = 1
            ai3posy = 0
            ai4posx = -1
            ai4posy = 0
            ai5posx = -1
            ai5posy = -1
            posx = 1
            posy = 1
            question = False
        else:
            print('Please enter one of the names provided below')
    except NameError:
        print("Wrong Character.")


#Initializes the background, score text, all four balls, win and loose images, the score itself, and ai sequences for all 5 ai profiles
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Achievement Hunter Pacman V.01")
myfont = pygame.font.SysFont("monospace", 24)
score = 0
scoretext = myfont.render("Score = "+str(score), 1, (255,79,0))
screen.blit(scoretext, (0,0))
jack = (-2,2,-2,2,-2,2)
geoff = (-3,3,-3,3,-3,3)
ryan = (-1,1,-1,1,-1,1)
ray = (-2,2)
gavin = (-1,1)
pacmanball1 = pygame.image.load("Pacman_Dot.png")
pacmanball2 = pygame.image.load("Pacman_Dot.png")
pacmanball3 = pygame.image.load("Pacman_Dot.png")
pacmanball4 = pygame.image.load("Pacman_Dot.png")
you_win = pygame.image.load("You_Win.png")
you_loose = pygame.image.load("You_Loose.png")



    
game = True    
        
#Main Game Loop        
while game == True:
    clock.tick(60) #Sets the FPS
    screen.blit(background, backgroundRect) #Creates the background
    scoretext = myfont.render("Score = "+str(score), 1, (255,79,0))
    screen.blit(scoretext, (0,0))
    
    
    for event in pygame.event.get(): #Checks for user clicking the Red X button to close game
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        elif event.type == KEYDOWN and event.key == K_RIGHT: #Checks for user input of Right Arrow Key
            #Assigns all character movement based upon user input of Right Arrow Key
            posx = 2
            posy = 0
            ai1posx = 0
            ai1posy = random.choice(jack)
            ai2posx = random.choice(geoff)
            ai2posy = 0
            ai3posx = random.choice(ryan)
            ai3posy = 0
            ai4posx = random.choice(ray)
            ai4posy = 0
            ai5posx = random.choice(gavin)
            ai5posy = 0
        elif event.type == KEYDOWN and event.key == K_LEFT:#Checks for user input of Left Arrow Key
            #Assigns all character movement based upon user input of Left Arrow Key
            posx = -2
            posy = 0
            ai1posx = random.choice(jack)
            ai1posy = 0
            ai2posx = random.choice(geoff)
            ai2posy = 0
            ai3posx = random.choice(ryan)
            ai3posy = 0
            ai4posx = random.choice(ray)
            ai4posy = 0
            ai5posx = random.choice(gavin)
            ai5posy = 0
        elif event.type == KEYDOWN and event.key == K_UP:#Checks for user input of Up Arrow Key
            #Assigns all character movement based upon user input of Up Arrow Key
            posy = -2
            posx = 0
            ai1posx = 0
            ai1posy = random.choice(jack)
            ai2posx = random.choice(geoff)
            ai2posy = 0
            ai3posx = random.choice(ryan)
            ai3posy = 0
            ai4posx = 0
            ai4posy = random.choice(ray)
            ai5posx = 0
            ai5posy = random.choice(gavin)
        elif event.type == KEYDOWN and event.key == K_DOWN:#Checks for user input of Right Down Key
            #Assigns all character movement based upon user input of Down Arrow Key
            posy = 2
            posx = 0
            ai1posx = 0
            ai1posy = random.choice(jack)
            ai2posx = random.choice(geoff)
            ai2posy = 0
            ai3posx = 0
            ai3posy = random.choice(ryan)
            ai4posx = random.choice(ray)
            ai4posy = 0
            ai5posx = 0
            ai5posy = random.choice(gavin)

        
       
    #Sends all of the positions to their respective class locations to move their charaters around the screen
    player_tuple = player1.update(posx,posy)
    ai_tuple = AI1.update(ai1posx,ai1posy)
    ai2_tuple = AI2.update(ai2posx,ai2posy)
    ai3_tuple = AI3.update(ai3posx,ai3posy)
    ai4_tuple = AI4.update(ai4posx,ai4posy)
    ai5_tuple = AI5.update(ai5posx,ai5posy)
    ball_list = ball.update(size[0],size[1])
    screen.blit(scoretext, (0,0))
    #Draws all Four Balls on the screen
    screen.blit(pacmanball1,(ball_list[0][0],ball_list[0][1]))
    screen.blit(pacmanball2,(ball_list[1][0],ball_list[1][1]))
    screen.blit(pacmanball3,(ball_list[2][0],ball_list[2][1]))
    screen.blit(pacmanball4,(ball_list[3][0],ball_list[3][1]))
    
    #Finds the difference in all of the player's distances to the AI
    difference1_of_x_values = player_tuple[0] - ai_tuple[0]
    difference1_of_y_values = player_tuple[1] - ai_tuple[1]
    difference2_of_x_values = player_tuple[0] - ai2_tuple[0]
    difference2_of_y_values = player_tuple[1] - ai2_tuple[1]
    difference3_of_x_values = player_tuple[0] - ai3_tuple[0]
    difference3_of_y_values = player_tuple[1] - ai3_tuple[1]
    difference4_of_x_values = player_tuple[0] - ai4_tuple[0]
    difference4_of_y_values = player_tuple[1] - ai4_tuple[1]
    difference5_of_x_values = player_tuple[0] - ai5_tuple[0]
    difference5_of_y_values = player_tuple[1] - ai5_tuple[1]
    
    #Finds the distance between the player's x axis and each ball's x axis
    difference_of_x_value_ball = player_tuple[0] - ball_list[0][0]
    difference_of_x_value_ball2 = player_tuple[0] - ball_list[1][0]
    difference_of_x_value_ball3 = player_tuple[0] - ball_list[2][0]
    difference_of_x_value_ball4 = player_tuple[0] - ball_list[3][0]

    #Finds the distance between the player's y axis and each ball's y axis
    difference_of_y_value_ball = player_tuple[1] - ball_list[0][1]
    difference_of_y_value_ball2 = player_tuple[1] - ball_list[1][1]
    difference_of_y_value_ball3 = player_tuple[1] - ball_list[2][1]
    difference_of_y_value_ball4 = player_tuple[1] - ball_list[3][1]

    #Collision Comparison Checks
    #If player's distance to any ai is close enough to where the pixels are touching, then points are subtracted until the player stops touching the ai
    if difference1_of_x_values <26 and difference1_of_x_values >-26 and difference1_of_y_values <128 and difference1_of_y_values >-128:
        score = score -1
        
    if difference2_of_x_values <26 and difference2_of_x_values >-26 and difference2_of_y_values <128 and difference2_of_y_values >-128:
        score = score -1

    if difference3_of_x_values <26 and difference3_of_x_values >-26 and difference3_of_y_values <128 and difference3_of_y_values >-128:
        score = score -1

    if difference4_of_x_values <26 and difference4_of_x_values >-26 and difference4_of_y_values <128 and difference4_of_y_values >-128:
        score = score -1

    if difference5_of_x_values <26 and difference5_of_x_values >-26 and difference5_of_y_values <128 and difference5_of_y_values >-128:
        score = score -1

    #If the player's distance is close enough to one of the balls, then the players score is added upon until the player stops touching the ball
    if difference_of_x_value_ball < 15 and difference_of_x_value_ball > -15 and difference_of_y_value_ball < 128 and difference_of_y_value_ball > -128:
        score = score +1

    if difference_of_x_value_ball2 < 15 and difference_of_x_value_ball2 > -15 and difference_of_y_value_ball2 < 30 and difference_of_y_value_ball2 > -30:
        score = score +1

    if difference_of_x_value_ball3 < 15 and difference_of_x_value_ball3 > -15 and difference_of_y_value_ball3 < 50 and difference_of_y_value_ball3 > -50:
        score = score +1

    if difference_of_x_value_ball4 < 15 and difference_of_x_value_ball4 > -15 and difference_of_y_value_ball4 < 100 and difference_of_y_value_ball4 > -100:
        score = score +1
    #Player wins if he scores over 500 points
    if score > 500:
        screen.blit(you_win,(200,400))
        if score > 501:
            pygame.stop()
        
    #Player looses if he losses all of his points to the AI           
    if score < 0:
        screen.blit(you_loose,(200,400))
        if score < -1:
            pygame.stop()
             
    #Refreshes the screen to display every frame of movement        
    pygame.display.update()

