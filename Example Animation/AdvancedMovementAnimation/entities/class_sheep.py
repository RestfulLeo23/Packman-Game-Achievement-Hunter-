import pygame
from pygame import *

import datetime
from datetime import datetime, timedelta

import config
from config import AppConfig

import lib_sprites
from lib_sprites import SpriteBase, SpriteDirection

class Sheep(SpriteBase):
    def __init__(self):
        super(Sheep, self).__init__()
        self.ImageSource(pygame.image.load('images/Animal.png'))
        
        #looking north
        self.HotSpots(pygame.Rect(320, 96, 32, 32)) #standing
        self.HotSpots(pygame.Rect(288, 96, 32, 32)) #step right foot
        self.HotSpots(pygame.Rect(352, 96, 32, 32)) #step left foot
        
        #looking east
        self.HotSpots(pygame.Rect(320, 64, 32, 32)) #standing
        self.HotSpots(pygame.Rect(288, 64, 32, 32)) #step right foot
        self.HotSpots(pygame.Rect(352, 64, 32, 32)) #step left foot
        
        #looking west
        self.HotSpots(pygame.Rect(320, 32, 32, 32)) #standing
        self.HotSpots(pygame.Rect(352, 32, 32, 32)) #step right foot
        self.HotSpots(pygame.Rect(288, 32, 32, 32)) #step left foot
        
        #looking south
        self.HotSpots(pygame.Rect(320, 0, 32, 32)) #standing
        self.HotSpots(pygame.Rect(288, 0, 32, 32)) #step right foot
        self.HotSpots(pygame.Rect(352, 0, 32, 32)) #step left foot
        
    #makes a sprite turn to specified direction
    def Turn(self, screen, direction):
        self.Direction(direction)
        index = -1
        
        if(direction == SpriteDirection.NORTH):
            index = 0
        elif(direction == SpriteDirection.EAST):
            index = 3
        elif(direction == SpriteDirection.WEST):
            index = 6
        elif(direction == SpriteDirection.SOUTH):
            index = 9
        screen.fill([255, 255, 255])
        self.RenderImage(screen, index)
        pygame.display.update()
        
    #makes a sprite walk to current direction
    def Walk(self, screen):
        locations = list() #contains locations for each sprite image to render in succession
        indexarray = None #contains the indices of all sprite images to render
        if(self.Direction() == SpriteDirection.NORTH):
            locations.append([self.Location()[0], self.Location()[1]-8])
            locations.append([self.Location()[0], self.Location()[1]-16])
            locations.append([self.Location()[0], self.Location()[1]-24])
            locations.append([self.Location()[0], self.Location()[1]-32])
            indexarray = [1, 2, 1, 0]
        elif(self.Direction() == SpriteDirection.EAST):
            locations.append([self.Location()[0]+8, self.Location()[1]])
            locations.append([self.Location()[0]+16, self.Location()[1]])
            locations.append([self.Location()[0]+24, self.Location()[1]])
            locations.append([self.Location()[0]+32, self.Location()[1]])
            indexarray = [4, 5, 4, 3]
        elif(self.Direction() == SpriteDirection.WEST):
            locations.append([self.Location()[0]-8, self.Location()[1]])
            locations.append([self.Location()[0]-16, self.Location()[1]])
            locations.append([self.Location()[0]-24, self.Location()[1]])
            locations.append([self.Location()[0]-32, self.Location()[1]])
            indexarray = [7, 8, 7, 6]
        elif(self.Direction() == SpriteDirection.SOUTH):
            locations.append([self.Location()[0], self.Location()[1]+8])
            locations.append([self.Location()[0], self.Location()[1]+16])
            locations.append([self.Location()[0], self.Location()[1]+24])
            locations.append([self.Location()[0], self.Location()[1]+32])
            indexarray = [10, 11, 10, 9]
            
        self.__animate_walk__(screen, locations, indexarray)
        
    #displays the series of images that will make the entity appear like it's walking
    def __animate_walk__(self, screen, locations, indexarray):
        if(len(locations) == 0 or len(indexarray) == 0):
            return
        #loops through the set locations and images and display them in a set interval
        for i in range(len(locations)):
            loc = locations[i]
            if(loc[0] < 0 or loc[1] < 0 or loc[0] > AppConfig.DEFAULT_SCREENSIZE[0]-32 or loc[1] > AppConfig.DEFAULT_SCREENSIZE[1]-32):
                return
            
            self.Location(loc)
            screen.fill([255, 255, 255])
            self.RenderImage(screen, indexarray[i])
            pygame.display.update()
            
            #implements 0.125 second delay
            t1 = datetime.now() + timedelta(seconds=0.125)
            while(datetime.now() < t1):
                pass
            self.Location(loc)