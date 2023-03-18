'''
* ==================================================================
* Description: scoreboard.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 17:08
* ===================================================================
'''
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    
    def __init__(self,ai_settings,screen,stats) -> None:
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        # set the fonts

        self.text_color=(30,30,30)
        self.font=pygame.font.SysFont(None,40)

        # primary score

        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()


    def prep_score(self):

        '''render the score text'''

        rounded_score=int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render("Score: "+score_str,True,self.text_color,None)

        # put the score at the top right corner

        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=20


    def prep_high_score(self):

        '''render the highest score'''

        high_score=int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render("Best: "+high_score_str,True,self.text_color,None)

        # place it on the top center

        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.x=self.screen_rect.left+10
        self.high_score_rect.bottom=self.screen_rect.bottom-10


    def show_score(self):

        '''show the score on the screen'''

        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)


    def prep_level(self):

        '''render the level'''

        self.level_image=self.font.render("Level: "+str(self.stats.level),True,self.text_color,None)

        #  place it below highest score

        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.bottom=self.screen_rect.bottom-10


    def prep_ships(self):

        '''the number of ships left'''

        self.ships=Group()

        for ship_number in range(self.stats.ship_left):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=10+ship_number*ship.rect.width
            ship.rect.y=10
            self.ships.add(ship)

