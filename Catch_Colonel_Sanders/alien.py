'''
* ==================================================================
* Description: alien.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:13
* ===================================================================
'''
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_settings,screen) -> None:
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        # load the image and set rect attribute

        self.image=pygame.image.load('./images/alien.bmp')
        self.rect=self.image.get_rect()

        # primary position

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)


    def check_edges(self):
        '''meet the edge,return True'''
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
        

    def update(self):
        '''move rightwards'''
        self.x += self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x=self.x


    def blitme(self):
        self.screen.blit(self.image,self.rect)