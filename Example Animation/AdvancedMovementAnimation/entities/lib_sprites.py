import pygame
from pygame import *

import sys
sys.path.append('utils')

import lib_utils
from lib_utils import StaticFunction

class SpriteDirection:
    NORTH = '+Y'
    EAST = '+X'
    WEST = '-X'
    SOUTH = '-Y'
    
    def IsDirection(direction):
        if(direction == SpriteDirection.NORTH or \
           direction == SpriteDirection.EAST or \
           direction == SpriteDirection.WEST or \
           direction == SpriteDirection.SOUTH):
            return True
        
        return False
    
    IsDirection = StaticFunction(IsDirection)

class SpriteBase(object):
    def __init__(self):
        self._imagesource = None
        self._hotspots = list()
        self._direction = SpriteDirection.SOUTH
        self._location = [0, 0]
        
    #Properties
    def ImageSource(self, imgsrc=None):
        if (imgsrc == None):
            return self._imagesource
        else:
            self._imagesource = imgsrc
            
    def HotSpots(self, rect=None):
        if(rect == None):
            return self._hotspots
        else:
            self._hotspots.append(rect)
            
    def Direction(self, direction=None):
        if(direction == None):
            return self._direction
        else:
            if(SpriteDirection.IsDirection(direction)):
                self._direction = direction
                
    def Location(self, location=None):
        if(location == None):
            return self._location
        else:
            self._location = location
    
    #Methods
    def RenderImage(self, screen, spotindex):
        screen.blit(self._imagesource, self._location, self._hotspots[spotindex])
        
    def RenderImageAtLocation(self, screen, location=None, spotindex=0):
        screen.blit(self._imagesource, location, self._hotspots[spotindex])