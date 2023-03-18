'''
* ==================================================================
* Description: settings.py
* Copyright (c) Konrad Locas.
* All rights reserved.
* Author: Konrad Locas.
* Date: 2023/03/16 15:13
* ===================================================================
'''
class Settings():
    def __init__(self) -> None:

        #screeen
         
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(249,243,229)

        # the ship

        self.ship_speed_factor=2
        self.ship_limit=3

        # the bullets

        self.bullet_speed_factor=4
        self.bullet_width=10
        self.bullet_height=15
        self.bullet_color=60,60,60
        self.bullet_allowed=6

        # the aliens

        self.alien_speed_factor=0.2
        self.fleet_drop_speed=6
        self.fleet_direction=1 # 1 for rightwards,-1 for leftwards

        # hasten the game

        self.speedup_scale=1.1

        # raise the points of each alien

        self.score_scale=1.5

        self.initialise_dynamic_settings()


    def initialise_dynamic_settings(self):
        
        '''initialise the settings'''
        
        self.ship_speed_factor=1.5
        self.bullet_speed_factor=3
        self.alien_speed_factor=0.5
        self.fleet_direction=1

        # record the score

        self.alien_points=50


    def increase_speed(self):

        '''hasten'''

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points=int(self.alien_points*self.score_scale)

        