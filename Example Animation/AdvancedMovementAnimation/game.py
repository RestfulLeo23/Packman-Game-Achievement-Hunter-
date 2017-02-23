import pygame
from pygame import *

import config
from config import AppConfig

import sys
sys.path.append('entities')

import lib_sprites
from lib_sprites import SpriteDirection

import class_sheep
from class_sheep import Sheep

import class_cow
from class_cow import Cow

import class_rooster
from class_rooster import Rooster

import class_butterfly
from class_butterfly import Butterfly

pygame.init()
pygame.key.set_repeat(1, 1)

screen = pygame.display.set_mode(AppConfig.DEFAULT_SCREENSIZE)
display.set_caption('Advanced Animation Demo')
screen.fill([255, 255, 255])
going = True

character = Sheep()
character.RenderImage(screen, 9)
pygame.display.update()

while going:
    for e in event.get():
        if e.type == QUIT: #checks if close button was clicked
            going = False
        elif e.type == KEYDOWN:
            keystate = pygame.key.get_pressed()
            if(keystate[K_UP]):
                if(character.Direction() == SpriteDirection.NORTH):
                    character.Walk(screen)
                else:
                    character.Turn(screen, SpriteDirection.NORTH)
            elif(keystate[K_RIGHT]):
                if(character.Direction() == SpriteDirection.EAST):
                    character.Walk(screen)
                else:
                    character.Turn(screen, SpriteDirection.EAST)
            elif(keystate[K_LEFT]):
                if(character.Direction() == SpriteDirection.WEST):
                    character.Walk(screen)
                else:
                    character.Turn(screen, SpriteDirection.WEST)
            elif(keystate[K_DOWN]):
                if(character.Direction() == SpriteDirection.SOUTH):
                    character.Walk(screen)
                else:
                    character.Turn(screen, SpriteDirection.SOUTH)

pygame.quit()