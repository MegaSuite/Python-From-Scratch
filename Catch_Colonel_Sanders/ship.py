'''
* ==================================================================
* Description: ship.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:12
* ===================================================================
'''
import pygame

from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen) -> None:

        # initialize
        super().__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        # load the image, get the rect

        self.image=pygame.image.load('./images/spaceship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # primary position of the ship

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.center=float(self.rect.centerx)

        # change the symbol

        self.move_right=False
        self.move_left=False

    def update(self):

        # restrict the ship in the visible range and move the ship

        if self.move_right and self.rect.right<self.screen_rect.right:
            self.center+=self.ai_settings.ship_speed_factor
        if self.move_left and self.rect.left>0:
            self.center-=self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center


    def blitme(self):

        '''draw the ship'''
        
        self.screen.blit(self.image,self.rect)

    
    def center_ship(self):
        '''center the ship'''
        self.center=self.screen_rect.centerx