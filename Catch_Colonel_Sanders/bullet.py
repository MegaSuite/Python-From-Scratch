'''
* ==================================================================
* Description: bullet.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:13
* ===================================================================
'''
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self,ai_settings,screen,ship) -> None:
        super().__init__()
        self.screen=screen

        # create a bullet on (0,0) and place it on a right position

        self.rect=pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        # store the position of bullet in float type

        self.y=float(self.rect.y)

        self.color=ai_settings.bullet_color
        self.speed_factor=ai_settings.bullet_speed_factor

    def update(self) -> None:
        
        # renew the float num of bullet's position

        self.y -= self.speed_factor

        # renew the position

        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)

